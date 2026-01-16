import pandas as pd
import numpy as np
from great_tables import GT, style, loc
from sklearn.datasets import load_wine
from IPython.display import HTML, display
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.preprocessing import StandardScaler
from GT_style import GTStyle


class WineDataset:
    _df: pd.DataFrame

    def __init__(self):
        self._prepare_df()

    def _prepare_df(self):
        wine = load_wine()
        self._df = pd.DataFrame(wine.data, columns=wine.feature_names)
        self._excluded_columns = ["cultivar", "cultivar_name"]
        self._target_column = "cultivar_name"
        self._df["cultivar"] = wine.target
        self._df["cultivar_name"] = self._df["cultivar"].map(
            {0: "Odrůda 1", 1: "Odrůda 2", 2: "Odrůda 3"}
        )

    def _get_stat_description(self):
        desc = {}
        desc["Počet vzorků"] = self._df.shape[0]
        desc["Počet proměnných"] = self._df.shape[1] - 2
        desc["Odrůdy"] = list(self._df["cultivar_name"].drop_duplicates())
        desc["Rozdělení tříd"] = (
            self._df[self._target_column].value_counts().sort_index().to_dict()
        )

        return desc

    def show_standardization_result(self):
        X = self._df.drop(columns=self._excluded_columns)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        html_code = f"""
        <div style="display: flex; flex-direction: column; gap: 20px;">
            {f"Průměr po standardizaci (měl by být ~0): {X_scaled.mean():.6f}<br>"}
            {f"Směrodatná odchylka po standardizaci (měla by být ~1): {X_scaled.std():.6f}<br>"}
        </div>
        """

        display(HTML(html_code))

    def show_missing_values(self):
        missing_values = self._df.isnull().sum().sum()
        html_code = f"""
        <div style="display: flex; flex-direction: column; gap: 20px;">
            {f"Chybějící hodnoty: {missing_values}<br>"}
        """
        if missing_values == 0:
            html_code += f"Dataset neobsahuje chybějící hodnoty"

        html_code += f"""</div>"""

        display(HTML(html_code))

    def show_eda(self):
        desc = self._get_stat_description()

        df_meta = pd.DataFrame(
            {
                "Vlastnost": ["Počet vzorků", "Počet proměnných"],
                "Hodnota": [desc["Počet vzorků"], desc["Počet proměnných"]],
            }
        )
        gt_meta = (
            GT(df_meta)
            .tab_header(title="Metadata datasetu")
            .tab_options(**GTStyle().style)
        )

        df_odrudy = pd.DataFrame({"Odrůda": desc["Odrůdy"]})
        gt_odrudy = (
            GT(df_odrudy)
            .tab_header(title="Seznam sledovaných odrůd")
            .cols_label(Odrůda="")
            .tab_options(**GTStyle().style)
        )

        df_counts = pd.DataFrame(
            list(desc["Rozdělení tříd"].items()), columns=["Odrůda", "Počet vzorků"]
        )
        gt_counts = (
            GT(df_counts)
            .tab_header(title="Rozdělení vzorků v třídách")
            .tab_options(**GTStyle().style)
        )

        desc_df = (
            self._df.describe().reset_index().rename(columns={"index": "Statistika"})
        )
        desc_df = desc_df.drop(columns=desc_df.columns[-1])
        cols_to_format = desc_df.select_dtypes(include=["number"]).columns.to_list()

        gt_desc = (
            GT(desc_df)
            .tab_header(title="Popisná statistika")
            .fmt_number(
                columns=cols_to_format,
                # decimals=2,
            )
            .tab_style(
                style=style.text(weight="bold"),
                locations=loc.body(columns="Statistika"),
            )
            .tab_options(**GTStyle().style)
        )

        html_code = f"""
        <div style="display: flex; flex-direction: column; gap: 20px;">
            {gt_meta._repr_html_()}
            {gt_odrudy._repr_html_()}
            {gt_counts._repr_html_()}
            {gt_desc._repr_html_()}
        </div>
        """

        display(HTML(html_code))

    def show_head(self):
        gt_head = (
            GT(self._df.head())
            .tab_header(title="Ukázka dat")
            .tab_options(**GTStyle().style)
        )

        html_code = f"""
        <div style="display: flex; flex-direction: column; gap: 20px;">
            {gt_head._repr_html_()}
        </div>
        """

        display(HTML(html_code))

    def show_corr_matrix(self):
        _, ax = plt.subplots(figsize=(14, 10))
        corr_matrix = self._df.iloc[:, :-2].corr()
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        sns.heatmap(
            corr_matrix,
            mask=mask,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            center=0,
            square=True,
            ax=ax,
            cbar_kws={"label": "Korelace"},
        )
        ax.set_title(
            "Korelační matice proměnných", fontsize=14, fontweight="bold", pad=20
        )
        plt.tight_layout()
        plt.show()

        # maska horniho trojuhelniku
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
        # nastaveni horniho trojuhelniku na NaN
        corr_matrix_lower = corr_matrix.where(~mask)

        corr_pairs = corr_matrix_lower.unstack()
        corr_pairs = corr_pairs.dropna()

        df_corr = corr_pairs.sort_values(ascending=False).head().reset_index()

        df_corr = df_corr.rename(columns={df_corr.columns[-1]: "Korelace"})
        labels = {col: "" for col in df_corr.columns}
        labels["Korelace"] = "Korelace"

        gt_corr = (
            GT(df_corr)
            .tab_header(title="Nejsilnější pozitivní korelace")
            .cols_label(labels)
            .fmt_number(
                columns=["Korelace"],
                decimals=4,
            )
            .tab_options(**GTStyle().style)
        )

        html_code = f"""
        <div style="display: flex; flex-direction: column; gap: 20px;">
            {gt_corr._repr_html_()}
        </div>
        """

        display(HTML(html_code))

    def show_histograms(self):
        features = features = self._df.columns.difference(
            self._excluded_columns
        ).tolist()

        size = list(plt.rcParams["figure.figsize"])
        size[1] = size[1] * len(features) * 0.5

        target_values = self._df[self._target_column].unique()
        n_colors = len(target_values)
        colors = plt.cm.rainbow(np.linspace(0, 1, n_colors))

        _, axes = plt.subplots(len(features), 1, figsize=size)

        for idx, feature in enumerate(features):
            ax = axes[idx]
            for i, target_value in enumerate(target_values):
                subset = self._df[self._df[self._target_column] == target_value][
                    feature
                ]
                ax.hist(subset, alpha=0.6, color=colors[i], label=target_value, bins=15)
            ax.set_xlabel(feature.replace("_", " ").title())
            ax.set_ylabel("Četnost")
            ax.legend()

        plt.suptitle(
            "Rozdělení vybraných proměnných podle odrůd",
            y=1.02,
        )
        plt.tight_layout()
        plt.show()

    @property
    def df(self):
        return self._df

    @property
    def excluded_columns(self):
        return self._excluded_columns
