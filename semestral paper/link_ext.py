import pandas as pd
import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from great_tables import GT, style, loc
from output_val_highlighter import *
from GT_style import GTStyle
from base_ext import ExtBase


class Link_ext(ExtBase):

    def __init__(
        self,
        data: pd.DataFrame,
        target_column,
        excluded_columns=[],
        method="ward",
        metric="euclidean",
    ):
        super().__init__(
            data=data, target_column=target_column, excluded_columns=excluded_columns
        )

        self._linkage_matrix = linkage(self._X, method=method, metric=metric)

    def show_dendrogram(self, truncate_mode=None, p=30):
        plt.figure(figsize=(12, 7))
        dendrogram(
            self._linkage_matrix,
            truncate_mode=truncate_mode,
            p=p,
            leaf_rotation=90.0,
            leaf_font_size=10.0,
            show_contracted=True,
        )

        plt.title("Hierarchické shlukování - Dendrogram", fontweight="bold")
        plt.xlabel("Index vzorku (nebo velikost shluku)")
        plt.ylabel("Vzdálenost (Dissimilarity)")
        plt.axhline(y=10, color="r", linestyle="--")  # Orientační čára pro řez
        plt.tight_layout()
        plt.show()

    def show_cluster_stats(self, n_clusters=3):
        # Přiřazení vzorků do shluků
        clusters = fcluster(
            self._linkage_matrix, self._get_target_values_count(), criterion="maxclust"
        )

        # Vytvoření křížové tabulky (Crosstab)
        df_compare = pd.crosstab(
            clusters,
            self._y,
            rownames=["Predikovaný Shluk"],
            colnames=["Skutečná Odrůda"],
        ).reset_index()

        gt = (
            GT(df_compare)
            .tab_header(
                title="Srovnání Shluků a Odrůd",
                subtitle=f"Rozdělení vzorků do {n_clusters} shluků pomocí metody Ward",
            )
            .pipe(GTStyle().apply)
        )

        self._display_gt_html([gt])
