import matplotlib.pyplot as plt
import seaborn as sns


def configure():
    # Nastavení globálního vizuálního stylu
    plt.rcParams.update(
        {
            # Odstranění horní a pravé linky (spines)
            "axes.spines.top": False,
            "axes.spines.right": False,
            # Mřížka
            "axes.grid": True,
            "grid.alpha": 0.3,
            "grid.color": "#d3d3d3",
            "grid.linestyle": "--",
            # Fonty a velikosti
            "axes.titlesize": 14,
            "axes.titleweight": "bold",
            "axes.labelsize": 11,
            "legend.fontsize": 10,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            # Výchozí velikost grafu
            "figure.figsize": (10, 6),
            "figure.titlesize": 16,
            "figure.facecolor": "#b8b8b8",  # Nastaví bílou pod suptitle
            # Legenda
            "legend.fontsize": 11,
            "legend.loc": "best",  # Automaticky vybere nejlepší místo
            "legend.frameon": True,  # Chceš kolem ní rámeček? (True/False)
            "legend.edgecolor": "#d3d3d3",  # Barva rámečku (světle šedá, aby nerušila)
            "legend.facecolor": "white",  # Pozadí legendy
            "legend.framealpha": 0.8,  # Průhlednost pozadí
            "legend.fancybox": True,  # Zaoblené rohy rámečku
        }
    )

    # Pokud používáš Seaborn, můžeš nastavit i jeho barevnou paletu
    sns.set_palette("viridis")
    sns.set_style("whitegrid")
