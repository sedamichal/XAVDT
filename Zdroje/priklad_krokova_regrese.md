# PRAKTICKÝ PŘÍKLAD KROKOVÉ REGRESE

## ZADÁNÍ

### Data: Předpověď ceny domu

**Závislá proměnná (Y):** Cena domu (v milionech Kč)

**Potenciální vysvětlující proměnné:**
- **X₁:** Plocha (m²)
- **X₂:** Počet pokojů
- **X₃:** Stáří domu (roky)
- **X₄:** Vzdálenost od centra (km)
- **X₅:** Má garáž? (0=ne, 1=ano)

**Rozsah:** n = 50 domů

**Úkol:** Najít nejlepší model pomocí krokové regrese.

---

## NASTAVENÍ KRITÉRIÍ

**F-to-entry:** F₁,₄₅(0.95) = **4,06** (α = 0.05)
- Pro **PŘIDÁNÍ** proměnné musí: F > 4,06

**F-to-remove:** F₁,₄₅(0.90) = **2,84** (α = 0.10)
- Pro **ODEBRÁNÍ** proměnné musí: F < 2,84

**Pravidlo:** F-to-remove < F-to-entry (aby nebyl cyklus!)

---

## KROK 0: VÝCHOZÍ STAV

### Model
```
ŷ = ȳ = 4.5 mil. Kč  (průměr)
```

**Žádné regresory!**

### Charakteristiky
- **TSS** = 450.0 (celková variabilita)
- **RSS** = 450.0 (nic nevysvětleno)
- **MSS** = 0.0
- **R²** = 0.000
- **s** = √(450/49) = 3.03 mil. Kč

### Korelace s Y

Spočítáme korelace všech proměnných s Y:

| Proměnná | r(Xᵢ, Y) | |r| | Pořadí |
|----------|----------|------|---------|
| X₁ (plocha) | +0.82 | 0.82 | 🥇 1. |
| X₂ (pokoje) | +0.65 | 0.65 | 3. |
| X₃ (stáří) | -0.71 | 0.71 | 2. |
| X₄ (vzdálenost) | -0.48 | 0.48 | 4. |
| X₅ (garáž) | +0.35 | 0.35 | 5. |

**→ Kandidát na první regresor: X₁ (nejvyšší |r|)**

---

## ITERACE 1: TESTOVÁNÍ X₁

### Model s X₁
```
ŷ = β₀ + β₁×X₁
```

### Odhady parametrů
```
ŷ = 0.85 + 0.044×plocha
```

### Charakteristiky
- **MSS** = 302.58 (vysvětleno)
- **RSS** = 147.42 (nevysvětleno)
- **R²** = 302.58/450.0 = **0.672** (67.2%)
- **s²** = 147.42/48 = 3.071
- **s** = 1.75 mil. Kč

### F-statistika pro X₁

**Parciální F:**
```
F₁ = MSS(X₁) / s²
F₁ = 302.58 / 3.071
F₁ = 98.52
```

**Kritérium:**
```
F₁ = 98.52 > F-to-entry = 4.06  ✓
```

**ROZHODNUTÍ:** ✅ **PŘIDÁNO X₁**

---

## KROK 1: MODEL S X₁

```
Model: ŷ = 0.85 + 0.044×plocha
```

**Zařazené:** X₁
**Nezařazené:** X₂, X₃, X₄, X₅

### Testování nezařazených

Pro každou nezařazenou proměnnou spočítáme **parciální korelaci** s Y (po očištění od vlivu X₁):

| Proměnná | r_parciální | ΔR² | ΔRSS | F-statistika |
|----------|-------------|-----|------|--------------|
| X₃ (stáří) | -0.58 | 0.201 | 90.45 | 45.23 🥇 |
| X₂ (pokoje) | +0.42 | 0.098 | 44.10 | 22.05 |
| X₄ (vzdálenost) | -0.31 | 0.052 | 23.40 | 11.70 |
| X₅ (garáž) | +0.18 | 0.019 | 8.55 | 4.28 |

### Výpočet F pro X₃ (stáří)

**Krok 1:** Fitujeme model s X₁ + X₃
```
ŷ = β₀ + β₁×plocha + β₃×stáří
```

**Krok 2:** Nový RSS
```
RSS(X₁, X₃) = 56.97
```

**Krok 3:** Snížení RSS
```
ΔRSS = RSS(X₁) - RSS(X₁, X₃)
ΔRSS = 147.42 - 56.97 = 90.45
```

**Krok 4:** F-statistika
```
F₃ = ΔRSS / s²
F₃ = 90.45 / 2.00    (s² z nového modelu)
F₃ = 45.23
```

**Kandidát:** X₃ má nejvyšší F = 45.23

**Kritérium:**
```
F₃ = 45.23 > F-to-entry = 4.06  ✓
```

**ROZHODNUTÍ:** ✅ **PŘIDÁNO X₃**

---

## KROK 2: MODEL S X₁, X₃

```
Model: ŷ = 2.15 + 0.038×plocha - 0.095×stáří
```

**Zařazené:** X₁, X₃
**Nezařazené:** X₂, X₄, X₅

### Charakteristiky
- **R²** = 0.873 (87.3%)
- **RSS** = 56.97
- **s²** = 56.97/47 = 1.212
- **s** = 1.10 mil. Kč

### A) Kontrola zařazených (můžeme něco vyhodit?)

Testujeme, co by se stalo, kdybychom odebrali každý zařazený regresor:

| Odebrat | RSS po odebrání | ΔRSS | F |
|---------|----------------|------|---|
| X₁ | 198.45 | 141.48 | 116.73 🔥 |
| X₃ | 147.42 | 90.45 | 74.63 🔥 |

**F-statistiky pro vypuštění:**
```
F(X₁) = 141.48 / 1.212 = 116.73
F(X₃) = 90.45 / 1.212 = 74.63

Minimum F = 74.63
```

**Kritérium:**
```
min(F) = 74.63 > F-to-remove = 2.84  ✓
```

**ROZHODNUTÍ:** ❌ **Žádný regresor se neodebere** (oba jsou významné)

### B) Testování nezařazených (přidat další?)

| Proměnná | ΔR² | ΔRSS | F-statistika |
|----------|-----|------|--------------|
| X₂ (pokoje) | 0.042 | 18.90 | 15.59 🥇 |
| X₅ (garáž) | 0.028 | 12.60 | 10.40 |
| X₄ (vzdálenost) | 0.015 | 6.75 | 5.57 |

**Kandidát:** X₂ má nejvyšší F = 15.59

**Kritérium:**
```
F₂ = 15.59 > F-to-entry = 4.06  ✓
```

**ROZHODNUTÍ:** ✅ **PŘIDÁNO X₂**

---

## KROK 3: MODEL S X₁, X₂, X₃

```
Model: ŷ = 1.85 + 0.032×plocha + 0.18×pokoje - 0.082×stáří
```

**Zařazené:** X₁, X₂, X₃
**Nezařazené:** X₄, X₅

### Charakteristiky
- **R²** = 0.915 (91.5%)
- **RSS** = 38.07
- **s²** = 38.07/46 = 0.827
- **s** = 0.91 mil. Kč

### A) Kontrola zařazených

| Odebrat | RSS po odebrání | ΔRSS | F |
|---------|----------------|------|---|
| X₁ | 142.35 | 104.28 | 126.08 🔥 |
| X₃ | 98.52 | 60.45 | 73.09 🔥 |
| X₂ | 56.97 | 18.90 | 22.85 🔥 |

```
Minimum F = 22.85 (X₂)
```

**Kritérium:**
```
min(F) = 22.85 > F-to-remove = 2.84  ✓
```

**ROZHODNUTÍ:** ❌ **Žádný regresor se neodebere**

### B) Testování nezařazených

| Proměnná | ΔR² | ΔRSS | F-statistika |
|----------|-----|------|--------------|
| X₅ (garáž) | 0.012 | 5.40 | 6.53 🥇 |
| X₄ (vzdálenost) | 0.008 | 3.60 | 4.35 |

**Kandidát:** X₅ má nejvyšší F = 6.53

**Kritérium:**
```
F₅ = 6.53 > F-to-entry = 4.06  ✓
```

**ROZHODNUTÍ:** ✅ **PŘIDÁNO X₅**

---

## KROK 4: MODEL S X₁, X₂, X₃, X₅

```
Model: ŷ = 1.62 + 0.030×plocha + 0.15×pokoje - 0.075×stáří + 0.42×garáž
```

**Zařazené:** X₁, X₂, X₃, X₅
**Nezařazené:** X₄

### Charakteristiky
- **R²** = 0.927 (92.7%)
- **RSS** = 32.67
- **s²** = 32.67/45 = 0.726
- **s** = 0.85 mil. Kč

### A) Kontrola zařazených

| Odebrat | RSS po odebrání | ΔRSS | F |
|---------|----------------|------|---|
| X₁ | 145.80 | 113.13 | 155.81 🔥 |
| X₃ | 95.40 | 62.73 | 86.40 🔥 |
| X₂ | 51.30 | 18.63 | 25.66 🔥 |
| X₅ | 38.07 | 5.40 | 7.44 🔥 |

```
Minimum F = 7.44 (X₅)
```

**Kritérium:**
```
min(F) = 7.44 > F-to-remove = 2.84  ✓
```

**ROZHODNUTÍ:** ❌ **Žádný regresor se neodebere**

### B) Testování nezařazených

| Proměnná | ΔR² | ΔRSS | F-statistika |
|----------|-----|------|--------------|
| X₄ (vzdálenost) | 0.004 | 1.80 | 2.48 |

**Kritérium:**
```
F₄ = 2.48 < F-to-entry = 4.06  ✗
```

**ROZHODNUTÍ:** ❌ **X₄ se NEPŘIDÁ** (není významná)

---

## KONEC: FINÁLNÍ MODEL

### ✅ Konečný model
```
Cena = 1.62 + 0.030×plocha + 0.15×pokoje - 0.075×stáří + 0.42×garáž
```

### 📊 Finální statistiky

| Charakteristika | Hodnota |
|----------------|---------|
| **Zařazené proměnné** | X₁, X₂, X₃, X₅ (4 regresory) |
| **R²** | 0.927 (92.7%) |
| **R²ₐdⱼ** | 0.920 |
| **RSS** | 32.67 |
| **s** | 0.85 mil. Kč |
| **F-test celého modelu** | F₄,₄₅ = 142.5, p < 0.001 |

### 📋 Tabulka koeficientů

| Proměnná | Koeficient | SE | t | p |
|----------|------------|-----|-----|-------|
| Konstanta | 1.62 | 0.45 | 3.60 | 0.001 |
| X₁ (plocha) | 0.030 | 0.002 | 12.48 | <0.001 |
| X₂ (pokoje) | 0.15 | 0.03 | 5.07 | <0.001 |
| X₃ (stáří) | -0.075 | 0.008 | -9.30 | <0.001 |
| X₅ (garáž) | 0.42 | 0.15 | 2.73 | 0.009 |

**Všechny koeficienty jsou statisticky významné!** ✓

---

## INTERPRETACE VÝSLEDKŮ

### 1. Plocha (X₁)
```
Koeficient: +0.030
```
**Interpretace:** Každý další m² zvýší cenu o **30 000 Kč** (při fixních ostatních proměnných).

### 2. Počet pokojů (X₂)
```
Koeficient: +0.15
```
**Interpretace:** Každý další pokoj zvýší cenu o **150 000 Kč**.

### 3. Stáří (X₃)
```
Koeficient: -0.075
```
**Interpretace:** Každý rok stáří sníží cenu o **75 000 Kč**.

### 4. Garáž (X₅)
```
Koeficient: +0.42
```
**Interpretace:** Přítomnost garáže zvýší cenu o **420 000 Kč**.

### 5. Vzdálenost (X₄)
```
NEBYLA ZAŘAZENA
```
**Interpretace:** Po zohlednění plochy, pokojů, stáří a garáže už vzdálenost **nepřidává** statisticky významnou informaci.

---

## PRŮBĚH KROKOVÉ REGRESE - SHRNUTÍ

### 📈 Vývoj R²

| Iterace | Proměnné | R² | ΔR² |
|---------|----------|-----|------|
| 0 | - | 0.000 | - |
| 1 | X₁ | 0.672 | +0.672 🔥 |
| 2 | X₁, X₃ | 0.873 | +0.201 🔥 |
| 3 | X₁, X₂, X₃ | 0.915 | +0.042 |
| 4 | X₁, X₂, X₃, X₅ | 0.927 | +0.012 |
| - | (X₄ odmítnuto) | - | - |

### 📉 Vývoj s (reziduální směrodatná odchylka)

| Iterace | s (mil. Kč) | Zlepšení |
|---------|-------------|----------|
| 0 | 3.03 | - |
| 1 | 1.75 | -42% 🔥 |
| 2 | 1.10 | -37% 🔥 |
| 3 | 0.91 | -17% |
| 4 | 0.85 | -7% |

**Pozorování:** Největší zlepšení po přidání X₁ a X₃!

---

## GRAFICKÉ ZOBRAZENÍ

### Graf 1: Vývoj R² během iterací

```
R²
1.0 │
    │
0.9 │              ●────●
    │           ●
0.8 │        ●
    │      
0.7 │   ●
    │  
    │●
0.0 └────────────────────────
    0   1   2   3   4   Iterace
```

### Graf 2: F-statistiky při přidávání

```
F
120│   ●
   │
100│
   │
 80│
   │       ●
 60│
   │
 40│
   │           ●
 20│               ●
   │                   ●
  0└─────────────────────────
     X₁  X₃  X₂  X₅  X₄
```

---

## POROVNÁNÍ S JINÝMI METODAMI

### Co kdyby jiná metoda?

**Forward (jen přidávání):**
```
→ Stejný výsledek: X₁, X₃, X₂, X₅
```

**Backward (start se všemi):**
```
Start: X₁, X₂, X₃, X₄, X₅
→ Odebráno X₄
→ Finální: X₁, X₂, X₃, X₅
```

**All Possible (nejlepší pro k=4):**
```
→ Nejlepší kombinace 4 proměnných:
   {X₁, X₂, X₃, X₅} s R² = 0.927 ✓
```

**→ V tomto případě všechny metody daly stejný výsledek!** 🎯

---

## VALIDACE MODELU

### 1. Kontrola předpokladů

**✓ Normalita residuí**
- Shapiro-Wilk test: p = 0.12 > 0.05 ✓
- QQ-plot: přibližně lineární ✓

**✓ Homoskedasticita**
- Graf residuí vs. ŷ: náhodný rozptyl ✓
- Breusch-Pagan test: p = 0.08 > 0.05 ✓

**✓ Multikolinearita**
| Proměnná | VIF |
|----------|-----|
| X₁ | 2.1 |
| X₂ | 1.8 |
| X₃ | 1.5 |
| X₅ | 1.3 |

Všechny VIF < 10 ✓

**✓ Autokorelace**
- Durbin-Watson = 2.05 ≈ 2 ✓

### 2. Vlivné body

**Cookova vzdálenost:**
- Maximum Cᵢ = 0.18 < 1 ✓
- Žádné extrémně vlivné body

---

## PRAKTICKÉ POUŽITÍ MODELU

### Příklad 1: Předpověď ceny

**Nový dům:**
- Plocha: 120 m²
- Pokoje: 4
- Stáří: 5 let
- Garáž: Ano (1)

**Výpočet:**
```
ŷ = 1.62 + 0.030×120 + 0.15×4 - 0.075×5 + 0.42×1
ŷ = 1.62 + 3.60 + 0.60 - 0.375 + 0.42
ŷ = 5.865 mil. Kč
```

**95% interval spolehlivosti:**
```
[5.865 ± 2.01×0.85] = [4.16 ; 7.57] mil. Kč
```

### Příklad 2: Srovnání variant

**Varianta A:** Bez garáže
```
ŷ = 5.865 - 0.42 = 5.445 mil. Kč
```

**Varianta B:** S garáží
```
ŷ = 5.865 mil. Kč
```

**Rozdíl:** 420 000 Kč (hodnota garáže)

---

## ZÁVĚRY

### ✅ Úspěchy
1. Model vysvětluje **92.7%** variability cen
2. Všechny zařazené proměnné jsou **významné**
3. Předpoklady jsou **splněny**
4. Model je **stabilní** (žádné vlivné body)

### ⚠️ Omezení
1. **X₄ (vzdálenost)** nebyla významná
   - Možná už je informace obsažena v jiných proměnných
   - Nebo není lineární vztah
2. Model platí jen v rozsahu dat
   - Plocha: 50-200 m²
   - Stáří: 0-50 let

### 💡 Doporučení
1. **Použít model** pro předpovědi v daném rozsahu
2. **Monitorovat** predikce na nových datech
3. **Pravidelně aktualizovat** s novými daty
4. **Zvážit nelinearity** (např. stáří²)

---

## KOMPLETNÍ POSTUP - KONTROLNÍ SEZNAM

### Fáze 1: Příprava ✓
- [x] Definovat Y a X proměnné
- [x] Zkontrolovat data (chybějící hodnoty, outliers)
- [x] Spočítat korelace
- [x] Nastavit kritéria (F-to-entry, F-to-remove)

### Fáze 2: Iterace ✓
Pro každou iteraci:
- [x] Testovat nezařazené (přidat?)
- [x] Testovat zařazené (odebrat?)
- [x] Zaznamenat R², s, F-statistiky

### Fáze 3: Výběr ✓
- [x] Prozkoumat průběh R²
- [x] Kontrolovat F-statistiky
- [x] Vybrat finální model

### Fáze 4: Validace ✓
- [x] Normalita residuí
- [x] Homoskedasticita
- [x] Multikolinearita (VIF)
- [x] Vlivné body (Cook's D)

### Fáze 5: Interpretace ✓
- [x] Význam koeficientů
- [x] Praktické použití
- [x] Omezení modelu

---

**Hotovo! Máte kompletní příklad krokové regrese od začátku do konce.** 🎯
