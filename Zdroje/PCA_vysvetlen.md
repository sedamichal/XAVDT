# Co je to PCA? - Kompletní vysvětlení

## TL;DR (Stručně)
**PCA = Principal Component Analysis (Analýza hlavních komponent)**

> Z mnoha proměnných vytvoří několik nových "super-proměnných", které zachycují nejvíc informace.

---

## Proč PCA potřebujeme?

### Problém: Příliš mnoho dimenzí

Máte **13 proměnných** (alcohol, flavonoidy, fenoly...)

```
13 proměnných = 13-dimenzionální prostor
```

**Problém:**
- ❌ Člověk nedokáže vizualizovat více než 3 dimenze
- ❌ Těžko se hledají vzory a vztahy
- ❌ Některé proměnné jsou korelované (redundantní informace)
- ❌ "Curse of dimensionality" - čím víc proměnných, tím hůř fungují modely

### Řešení: PCA

```
13 proměnných → PCA → 2-3 hlavní komponenty
```

**Výhody:**
- ✅ Lze vizualizovat (2D, 3D graf)
- ✅ Zachováno 55-67% informace
- ✅ Odstranění korelací
- ✅ Odhalení hlavních faktorů variability

---

## Jak PCA funguje? (Krok za krokem)

### 1. STANDARDIZACE DAT
```
Proměnná před: alkohol = 11-15%, prolin = 278-1680 mg/L
                ↓
Proměnná po:   průměr = 0, směrodatná odchylka = 1
```
**Proč?** Jinak by proměnná s větším rozsahem "přebila" ostatní.

### 2. HLEDÁNÍ HLAVNÍCH SMĚRŮ

PCA hledá směry v datech, kde je **největší variabilita** (rozptyl).

**Analogie: Fotografie sochy**
- Máte sochu uprostřed místnosti
- Chcete ji vyfotit ze všech stran (13 fotek)
- PCA najde 2-3 **nejlepší úhly**, ze kterých vidíte nejvíc detailů
- Zbylé fotky by byly skoro stejné

**V datech:**
```
PC1 = směr s NEJVĚTŠÍ variabilitou (36.2%)
PC2 = směr s DRUHOU největší variabilitou (19.2%)
PC3 = směr s TŘETÍ největší variabilitou (11.1%)
...
```

### 3. PROJEKCE DAT

Data se "otočí" do nového souřadného systému (PC1, PC2, PC3...).

```
Původně:  [alkohol, flavonoidy, fenoly, ...]
          ↓ PCA transformace
Nově:     [PC1, PC2, PC3]
```

---

## Praktický příklad: Wine dataset

### Před PCA:
```
13 proměnných → nelze vizualizovat
```

### Po PCA:
```
2 hlavní komponenty → lze nakreslit 2D graf
```

### Co PCA našla?

**PC1 (36.2% variability):**
- Hlavně **flavonoidy** (0,92)
- Celkové **fenoly** (0,86)
- **OD280/OD315** (0,82)

**Interpretace:**  
PC1 = "Fenolický faktor" → Víno s vysokým PC1 má hodně fenolů, flavonoidů

**PC2 (19.2% variability):**
- Různé jiné chemické vlastnosti

**Celkem PC1 + PC2 = 55.4% informace**

---

## Klíčové pojmy

### 1. Hlavní komponenta (Principal Component, PC)
- Nová "super-proměnná"
- Lineární kombinace původních proměnných
- Příklad: `PC1 = 0,92×flavonoidy + 0,86×fenoly + 0,82×OD280/OD315 + ...`

### 2. Vysvětlený rozptyl (Explained Variance)
- % variability zachycené komponentou
- PC1 má vždy NEJVYŠŠÍ vysvětlený rozptyl
- Příklad: PC1 = 36.2%, PC2 = 19.2%

### 3. Loadings
- "Váhy" původních proměnných v PC
- Ukazují, které proměnné jsou důležité pro danou PC
- Vysoké loading → proměnná silně přispívá k PC

### 4. Scores
- Hodnoty vzorků v PC prostoru
- To, co vidíte na grafu PCA
- Každý vzorek má score pro PC1, PC2, PC3...

### 5. Scree plot
- Graf vysvětleného rozptylu pro každou PC
- Pomáhá rozhodnout, kolik PC si ponechat
- Hledáme "loket" (kde je velký pokles)

---

## Kdy použít PCA?

### ✅ Použít PCA když:
1. Máte **mnoho proměnných** (>5)
2. Chcete **vizualizovat** data
3. Proměnné jsou **korelované**
4. Chcete najít **hlavní faktory** variability
5. Potřebujete **redukovat dimenzi** pro machine learning

### ❌ Nepoužívat PCA když:
1. Máte **málo proměnných** (2-3) - není co redukovat
2. Proměnné **nejsou korelované** - PCA nic neušetří
3. Potřebujete **interpretovatelné** původní proměnné
4. Máte **supervised learning** s třídami → použijte LDA místo PCA

---

## PCA vs. jiné metody

| Metoda | Typ | Používá třídy? | Účel |
|--------|-----|----------------|------|
| **PCA** | Unsupervised | ❌ Ne | Redukce dimenze, vizualizace |
| **LDA** | Supervised | ✅ Ano | Maximální separace tříd |
| **t-SNE** | Unsupervised | ❌ Ne | Vizualizace shluků (nelineární) |
| **K-means** | Unsupervised | ❌ Ne | Hledání shluků |

---

## Interpretace výsledků PCA

### Biplot (scatter + loadings)
```
      PC2 ↑
          |     • ← Odrůda 1 (vysoké flavonoidy)
          |   •
    ------+------→ PC1 (flavonoidy, fenoly)
          | •
          |   • ← Odrůda 3 (nízké flavonoidy)
```

**Co vidíme:**
- Vzorky blízko sebe = podobné chemické složení
- Vzorky daleko = odlišné chemické složení
- Šipky (loadings) = vliv původních proměnných

### Scree plot
```
Rozptyl
  40% |█
  30% |█
  20% |  █
  10% |    █ ← "loket" → stačí 2-3 komponenty
   0% |      █ █ █ █ ...
      +------------------
       PC1 PC2 PC3 PC4 ...
```

**Pravidlo:**
- Ponechat PC, které vysvětlují >10% rozptylu
- Nebo dokud kumulativní rozptyl dosáhne ~80%
- V našem případě: **2-3 komponenty stačí**

---

## Matematika za PCA (zjednodušeně)

### Krok 1: Kovariační matice
```
Cov(X) = jak spolu proměnné korelují
```

### Krok 2: Vlastní čísla a vlastní vektory
```
Vlastní vektor = směr PC
Vlastní číslo = vysvětlený rozptyl
```

### Krok 3: Projekce
```
PC_scores = X × eigenvectors
```

**Nemusíte to počítat ručně!** → `sklearn.decomposition.PCA` to udělá za vás.

---

## Praktické tipy

### 1. Vždy standardizovat!
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### 2. Zkontrolovat vysvětlený rozptyl
```python
pca = PCA()
pca.fit(X_scaled)
print(pca.explained_variance_ratio_)
# Chceme alespoň 70-80% kumulativně
```

### 3. Vizualizovat biplot
- Scatter vzorků v PC prostoru
- Šipky loadings → které proměnné jsou důležité

### 4. Interpretovat PC
- Podívat se na loadings
- Pojmenovat PC podle dominantních proměnných
- Příklad: PC1 = "Fenolický faktor"

---

## Příklad kódu

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1. Standardizace
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 3. Vysvětlený rozptyl
print(f"PC1: {pca.explained_variance_ratio_[0]*100:.1f}%")
print(f"PC2: {pca.explained_variance_ratio_[1]*100:.1f}%")

# 4. Vizualizace
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.show()

# 5. Loadings (příspěvky proměnných)
loadings = pca.components_.T
print(loadings)
```

---

## Časté otázky (FAQ)

### Q: Kolik komponent si ponechat?
**A:** Dokud kumulativní rozptyl dosáhne 70-80%, nebo dokud jednotlivá PC vysvětluje >10%.

### Q: Ztratím informaci?
**A:** Ano, ale málo. V našem případě 2 PC = 55% info, 3 PC = 67% info. Zbylých 33-45% je "šum".

### Q: Jak interpretovat PC?
**A:** Podívat se na loadings → které proměnné mají nejvyšší hodnoty. PC1 v wine = flavonoidy + fenoly.

### Q: PCA vs. LDA?
**A:** PCA = unsupervised (nehledí na třídy), LDA = supervised (maximalizuje separaci tříd).

### Q: Můžu použít PCA na kategoriální data?
**A:** Ne přímo. Musíte je nejdřív převést na číselné (one-hot encoding) nebo použít jiné metody (MCA).

---

## Shrnutí

### ✅ CO JE PCA:
- Metoda pro **redukci dimenzionality**
- Vytvoří nové proměnné (PC), které zachycují **max. variabilitu**
- **Unsupervised** - nehledí na třídy

### ✅ PROČ PCA:
- Vizualizace vysokodimenzionálních dat
- Odstranění korelací mezi proměnnými
- Identifikace hlavních faktorů variability
- Předzpracování pro machine learning

### ✅ JAK NA TO:
1. Standardizovat data
2. Aplikovat PCA
3. Vybrat počet komponent (scree plot)
4. Interpretovat (loadings, biplot)

### ✅ V WINE DATASETU:
- **13 proměnných → 2 PC (55% info)**
- **PC1 = "Fenolický faktor"** (flavonoidy, fenoly)
- Umožnilo vizualizaci a identifikaci vzorů

---

## Reference a další zdroje

- Jolliffe, I. T. (2002). Principal Component Analysis (2nd ed.). Springer.
- Scikit-learn dokumentace: https://scikit-learn.org/stable/modules/decomposition.html#pca
- StatQuest video: "Principal Component Analysis (PCA), Step-by-Step"
