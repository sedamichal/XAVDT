import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from great_tables import GT, style, loc
from output_val_highlighter import *
from GT_style import GTStyle
from base_ext import ExtBase


class PCAExt(ExtBase):

    def __init__(self, data: pd.DataFrame, target_column, excluded_columns=[], n_components=None):

        super().__init__(
            data=data, target_column=target_column, excluded_columns=excluded_columns
        )

        self._pca = PCA(n_components=n_components)
        self._pca = self._pca.fit(self._X)
        self._styles_eigenvectors = self._prepare_styles_eigenvectors()
        self._styles_eigenvalues = self._prepare_styles_eigenvalues()

    @property
    def pca(self):
        return self._pca

    def _prepare_styles_eigenvectors(self) -> OutputStyleDict:
        styles = OutputStyleDict()
        styles[0] = OutputStyle(
            bg_color="WhiteSmoke", fg_color="red", text_wieght="bold"
        )
        styles[1] = OutputStyle(
            bg_color="WhiteSmoke", fg_color="brown", text_wieght="bold"
        )
        styles[2] = OutputStyle(
            bg_color="WhiteSmoke", fg_color="green", text_wieght="bold"
        )
        styles[3] = OutputStyle(
            bg_color="WhiteSmoke", fg_color="blue", text_wieght="bold"
        )

        return styles

    def _prepare_styles_eigenvalues(self) -> OutputStyleDict:
        styles = OutputStyleDict()
        styles[0] = OutputStyle(fg_color="red", text_wieght="bold")

        return styles

    def get_kaiser_criterion_pcs(self):
        df = self._get_eigenvaules_df()
        return df[df["Eigenvalue"] >= 1]

    def show_eigenvalues(self):
        df = self._get_eigenvaules_df()
        df_reset = df.reset_index().rename(
            columns={
                "Eigenvalue": "Vlastní číslo",
                "Individual %": "%",
                "Cumulative %": "Kumulativní %",
            }
        )

        numeric_cols = df_reset.select_dtypes(include=["number"]).columns.tolist()
        gt = (
            GT(df_reset)
            .tab_header(title="Vlastní čísla")
            .fmt_number(columns=numeric_cols)
            .fmt_number(
                columns=[col for col in df_reset.columns if "%" in col], decimals=0
            )
            .fmt_nanoplot(columns="%", plot_type="bar", autoscale=True)
            .pipe(GTStyle().apply)
        )

        gt = ValHighliter(
            columns_mask="*",
            th_column_mask="Vlastní číslo",
            treshold=1,
            lower=False,
            styles=self._prepare_styles_eigenvalues(),
        ).apply(df=df_reset, gt=gt)

        self._display_gt_html([gt])

    def _sort_pc_columns(self, df):
        def extract_pc_number(col_name):
            match = re.search(r"PC(\d+)", col_name)
            if match:
                return int(match.group(1))
            return 999

        # Seřadíme názvy sloupců nejdříve podle čísla PC a pak podle délky/obsahu
        # (aby PC1 bylo před PC1_% a to před PC1_%_CSUM)
        sorted_cols = sorted(df.columns, key=lambda x: (extract_pc_number(x), x))

        return df[sorted_cols]

    def prepare_biplot(
        self, ax, pca_index1=1, pca_index2=2, title="PCA Biplot"
    ):
        index1 = pca_index1 - 1
        index2 = pca_index2 - 1

        colors_map = self._get_colors_map()

        X_pca = self._pca.transform(self._X)

        for _, (color, column_value) in enumerate(colors_map):
            mask = self._data[self._target_column] == column_value
            ax.scatter(
                X_pca[mask, index1],
                X_pca[mask, index2],
                color=color,
                label=column_value,
                alpha=0.6,
                edgecolors="black",
                linewidth=0.5,
                s=60,
            )

        scale_factor = 3
        loadings = self._get_eigenvectors()

        for i, feature in enumerate(self._feature_names):
            x_val = loadings[i, index1] * scale_factor
            y_val = loadings[i, index2] * scale_factor

            ax.arrow(
                0,
                0,
                x_val,
                y_val,
                head_width=0.1,
                head_length=0.1,
                fc="darkgray",
                ec="darkgray",
                alpha=0.7,
            )
            ax.text(
                x_val,
                y_val,
                feature.replace("_", " "),
                ha="center",
                va="center",
                fontsize=8,
            )

        ax.set_xlabel(
            f"PC{pca_index1} ({self._pca.explained_variance_ratio_[index1]*100:.1f}%)",
            fontsize=12,
        )
        ax.set_ylabel(
            f"PC{pca_index2} ({self._pca.explained_variance_ratio_[index2]*100:.1f}%)",
            fontsize=12,
        )
        ax.set_title(title)
        # ax.legend(loc="best")
        # ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color="k", linewidth=0.5)
        ax.axvline(x=0, color="k", linewidth=0.5)

    def show_biplot(self, pca_index1=1, pca_index2=2):
        _, ax = plt.subplots()

        self.prepare_biplot(
            ax=ax,
            pca_index1=pca_index1,
            pca_index2=pca_index2,
        )

        plt.tight_layout()
        plt.show()

    def show_eigenvectors(self):
        df = self._get_eigenvectors_df()

        df_reset = df.reset_index().rename(columns={"index": "Vlastnost"})

        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        gt = (
            GT(df_reset)
            .tab_header(title="Vlastní vektory")
            .tab_style(
                style=style.text(weight="bold"),
                locations=loc.body(columns="Vlastnost"),
            )
            .fmt_number(columns=numeric_cols, decimals=2)
            .fmt_number(columns=[col for col in df.columns if "%" in col], decimals=0)
            .pipe(GTStyle().apply)
        )
        gt = ValHighliter(
            columns_mask="PC*",
            th_column_mask="PC*_%_CSUM",
            treshold=61,
            styles=self._prepare_styles_eigenvectors(),
        ).apply(df=df_reset, gt=gt)

        return gt

    def _get_eigenvaules(self):
        return np.array(self._pca.explained_variance_)

    def _get_eigenvaules_df(self):
        eigenvalues = self._get_eigenvaules()
        total = eigenvalues.sum()
        individual_percent = (eigenvalues / total) * 100
        cumulative_percent = np.cumsum(individual_percent)

        df = pd.DataFrame(
            {
                "Eigenvalue": eigenvalues,
                "Individual %": individual_percent,
                "Cumulative %": cumulative_percent,
            }
        )
        df.index = range(1, len(eigenvalues) + 1)
        df.index.name = "PC"

        return df

    def _get_eigenvectors(self):
        return self._pca.components_.T[:, :] * np.sqrt(self._pca.explained_variance_)

    def _get_eigenvectors_df(self):
        df_values = self.get_kaiser_criterion_pcs()
        loadings = self._get_eigenvectors()

        data = {}
        for i in df_values.index:
            pc_name = f"PC{i}"

            # Loading
            data[pc_name] = loadings[:, i - 1]

            # % příspěvek
            abs_loadings = np.abs(loadings[:, i - 1])
            total = abs_loadings.sum()
            contributions_pct = (abs_loadings / total) * 100
            data[f"{pc_name}_%"] = contributions_pct

        df = pd.DataFrame(data, index=self._feature_names)

        for col in [col for col in df.columns if "_%" in col]:
            df = df.sort_values(col, ascending=False)
            df[f"{col}_CSUM"] = df[col].cumsum()

        df = df.sort_index()
        df = self._sort_pc_columns(df)

        return df
