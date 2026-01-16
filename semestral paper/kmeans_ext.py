import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    adjusted_rand_score,
    silhouette_score,
)
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from output_val_highlighter import *
from pca_extended import PCAExt
from GT_style import GTStyle
from base_ext import ExtBase


class KMeansExt(ExtBase):

    def __init__(
        self,
        data: pd.DataFrame,
        target_column,
        excluded_columns=[],
        n_clusters=8,
        random_state=42,
    ):
        super().__init__(
            data=data, target_column=target_column, excluded_columns=excluded_columns
        )

        self._random_state = random_state
        self._kmeans = KMeans(n_clusters=n_clusters, random_state=self._random_state)
        self._clusters = self._kmeans.fit_predict(self._X)

    def get_metrics(self) -> dict[str, float]:
        res = {}
        res["ari"] = adjusted_rand_score(
            self._data[self._target_column], self._clusters
        )
        res["silhouette"] = silhouette_score(self._X, self._clusters)
        return res

    def _prepare_biplot(self, ax1, ax2):
        metrics = self.get_metrics()

        pca = PCAExt(
            data=self._data,
            target_column=self._target_column,
            excluded_columns=self._excluded_columns,
            n_components=2,
        )
        pca.prepare_biplot(
            ax=ax1,
            pca_index1=1,
            pca_index2=2,
            title="Původní třídy (skutečné odrůdy)",
        )
        centers_pca = pca.pca.transform(self._kmeans.cluster_centers_)
        X_pca = pca.pca.transform(self._X)

        # K-means shluky
        scatter = ax2.scatter(
            X_pca[:, 0],
            X_pca[:, 1],
            c=self._clusters,
            cmap="viridis",
            alpha=0.6,
            edgecolors="black",
            linewidth=0.5,
            s=60,
        )
        ax2.scatter(
            centers_pca[:, 0],
            centers_pca[:, 1],
            c="red",
            marker="X",
            s=300,
            edgecolors="black",
            linewidth=2,
            label="Centra",
        )

        ax2.set_xlabel(
            f"PC1 ({pca.pca.explained_variance_ratio_[0]*100:.1f}%)",
            fontsize=12,
        )
        ax2.set_ylabel(
            f"PC2 ({pca.pca.explained_variance_ratio_[1]*100:.1f}%)",
            fontsize=12,
        )

        ax2.set_title(
            f"K-means shluky (ARI={metrics["ari"]:.3f})", fontsize=14, fontweight="bold"
        )
        # ax2.grid(True, alpha=0.3)
        ax2.axhline(y=0, color="k", linewidth=0.5)
        ax2.axvline(x=0, color="k", linewidth=0.5)

        # 1. Vytvoříme divider pro aktuální osu
        divider = make_axes_locatable(ax2)

        # 2. Přidáme novou osu "pod" (bottom) stávající osu
        # size="5%" určuje tloušťku colorbaru, pad=0.5 mezeru od grafu
        cax = divider.append_axes("bottom", size="5%", pad=0.7)

        # 3. Vykreslíme colorbar do této specifické osy (cax)
        plt.colorbar(scatter, cax=cax, orientation="horizontal", label="Shluk")

    def show_biplot(self):
        size = list(plt.rcParams["figure.figsize"])
        size[1] = size[1] * 2

        _, (ax1, ax2) = plt.subplots(2, 1, figsize=size)
        self._prepare_biplot(ax1, ax2)
        plt.tight_layout()
        plt.show()

    def _get_data_for_kmeans(self):
        X = self._data.drop(columns=self._excluded_columns)
        scaler = StandardScaler()
        return scaler.fit_transform(X)

    def show_contingency(self):
        y = self._data[self._excluded_columns[0]].to_list()
        contingency = pd.crosstab(
            y, self._clusters, rownames=["Skutečná třída"], colnames=["K-means shluk"]
        )

        gt = (
            GT(contingency)
            .tab_header(
                title="Kontingenční tabulka (skutečné třídy vs. K-means shluky):"
            )
            .pipe(GTStyle().apply)
        )

        self._display_gt_html([gt])


class KMeansBruteForce:

    def __init__(
        self,
        data: pd.DataFrame,
        target_column,
        n_components_tab,
        excluded_columns=[],
        random_state=42,
    ):
        self._data = data
        self._target_column = target_column
        self._n_components_tab = n_components_tab
        self._random_state = random_state
        self._excluded_columns = excluded_columns
        self._kms = self._prepare()
        self._style = self._prepare_style()

    def _prepare(self):
        res = {}

        for i in self._n_components_tab:
            res[i] = KMeansExt(
                data=self._data,
                excluded_columns=self._excluded_columns,
                target_column=self._target_column,
                n_clusters=i,
                random_state=self._random_state,
            )

        return res

    def _get_metrics(self):
        tmp = {}

        for i, km in self._kms.items():
            tmp[i] = km.get_metrics()

        df_results = pd.DataFrame.from_dict(tmp, orient="index")
        df_results.index.name = "n_clusters"

        return df_results

    def _prepare_style(self):
        return OutputStyle(fg_color="red", text_wieght="bold")

    def show_metrics(self):
        df = self._get_metrics()
        df = df.reset_index().rename(
            columns={"n_clusters": "Počet clusterů", "ari": "ARI", "silhouette": "SIL"}
        )

        numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
        gt = (
            GT(df)
            .fmt_number(columns=numeric_cols[1:], decimals=2)
            .tab_header(title="Metriky podle počtu clusterů")
            .pipe(GTStyle().apply)
        )
        gt = MaxValueRowHighliter(value_column="ARI", style=self._style).apply(
            df=df, gt=gt
        )

        return gt
