import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
)
from great_tables import GT, style, loc
from GT_style import GTStyle
from base_ext import ExtBase


class LDA_ext(ExtBase):
    def __init__(
        self, data: pd.DataFrame, target_column, n_components: int, excluded_columns=[]
    ):
        super().__init__(
            data=data, target_column=target_column, excluded_columns=excluded_columns
        )
        self._lda = LinearDiscriminantAnalysis(n_components=n_components)
        self._X_lda = self._lda.fit_transform(self._X, self._y)
        self._accuracy = self._lda.score(self._X, self._y)

    def _get_prediction(self):
        y_pred = self._lda.predict(self._X)
        cm = confusion_matrix(self._y, y_pred)
        return y_pred, cm

    def show_accuracy(self):
        df_res = pd.DataFrame(
            self._lda.explained_variance_ratio_[:2],  # Vezmeme první dvě hodnoty
            index=["LD1", "LD2"],
            columns=["Vysvětlený rozptyl diskriminačními funkcemi"],
        )
        df_res = df_res.reset_index()

        cols_to_format = df_res.select_dtypes(include=["number"]).columns.to_list()
        gt = (
            GT(df_res, rowname_col="index")
            .tab_header(f"Přesnost klasifikace (LDA): {self._accuracy*100:.2f}%")
            .tab_options(**GTStyle().style)
            .fmt_number(columns=cols_to_format)
        )

        self._display_gt_html([gt])

    def show_prediction(self):
        y_pred, cm = self._get_prediction()

        _, ax = plt.subplots()
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=["Odrůda 1", "Odrůda 2", "Odrůda 3"],
            yticklabels=["Odrůda 1", "Odrůda 2", "Odrůda 3"],
            cbar_kws={"label": "Počet vzorků"},
        )
        ax.set_xlabel("Predikovaná třída")
        ax.set_ylabel("Skutečná třída")
        ax.set_title("Konfuzní matice - LDA")
        plt.tight_layout()
        plt.show()

        # 1. Získání reportu jako slovníku
        report_dict = classification_report(
            self._y,
            y_pred,
            target_names=self._get_target_values(),
            output_dict=True,
        )

        # 2. Převod na DF a transpozice
        # .T prohodí metriky do sloupců a třídy do řádků
        df_report = pd.DataFrame(report_dict).T.reset_index()

        # 3. Přejmenování sloupců pro přehlednost
        df_report.columns = [
            "Třída / Metrika",
            "Precision",
            "Recall",
            "F1-Score",
            "Support",
        ]

        # 4. Vizualizace
        gt_report = (
            GT(df_report)
            .tab_header(title="Klasifikační Report")
            .tab_options(**GTStyle().style)
            # Zaokrouhlení metrik (první 4 sloupce jsou float)
            .fmt_number(columns=["Precision", "Recall", "F1-Score"], decimals=3)
            # Support je vždy celé číslo (počet vzorků)
            .fmt_integer(columns="Support")
            # Zvýraznění názvů tříd v prvním sloupci
            .tab_style(
                style=style.text(weight="bold"),
                locations=loc.body(columns="Třída / Metrika"),
            )
        )
        self._display_gt_html([gt_report])

    def show_projection(self):
        _, ax = plt.subplots()

        colors_map = self._get_colors_map()

        for _, (color, target_value) in enumerate(colors_map):
            mask = self._y == target_value
            ax.scatter(
                self._X_lda[mask, 0],
                self._X_lda[mask, 1],
                c=color,
                label=target_value,
                alpha=0.6,
                edgecolors="black",
                linewidth=0.5,
                s=80,
            )

        ax.set_xlabel(f"LD1 ({self._lda.explained_variance_ratio_[0]*100:.1f}%)")
        ax.set_ylabel(f"LD2 ({self._lda.explained_variance_ratio_[1]*100:.1f}%)")
        ax.set_title(
            f"LDA - Lineární diskriminační analýza (Přesnost: {self._accuracy*100:.1f}%)"
        )
        ax.axhline(y=0, color="k", linewidth=0.5)
        ax.axvline(x=0, color="k", linewidth=0.5)

        plt.tight_layout()
        plt.show()

    def show_main_variables(self):
        lda_scaling = pd.DataFrame(
            self._lda.scalings_,
            columns=["LD1", "LD2"],
            index=self._feature_names.to_list(),
        )

        cols_to_format = lda_scaling.select_dtypes(include=["number"]).columns.to_list()
        gt1 = (
            GT(
                lda_scaling.sort_values("LD1", key=abs, ascending=False)
                .head()
                .reset_index()
            )
            .tab_header(title=f"Nejvýznamnější rysy pro LD1")
            .fmt_number(columns=cols_to_format)
            .pipe(GTStyle().apply)
        )
        gt2 = (
            GT(
                lda_scaling.sort_values("LD2", key=abs, ascending=False)
                .head()
                .reset_index()
            )
            .fmt_number(columns=cols_to_format)
            .tab_header(title=f"Nejvýznamnější rysy pro LD2")
            .pipe(GTStyle().apply)
        )

        self._display_gt_html([gt1, gt2])
