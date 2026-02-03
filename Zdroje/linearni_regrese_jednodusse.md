# LINEÁRNÍ REGRESE - ZJEDNODUŠENĚ

## Co je to lineární regrese?

**Lineární regrese** = hledání **rovnice přímky** (nebo roviny), která nejlépe popisuje vztah mezi proměnnými.

### Jednoduchý příklad
Chcete předpovědět **plat** (Y) na základě **let praxe** (X):
```
Plat = konstanta + koeficient × roky_praxe + chyba
```

---

## 1. ZÁKLADNÍ MODEL

### Matematický zápis

**Pro jeden bod:**
```
yᵢ = β₀ + β₁·x₁ᵢ + β₂·x₂ᵢ + ... + βₖ·xₖᵢ + εᵢ
```

**Co znamenají symboly:**
- **yᵢ** = pozorovaná hodnota (to, co chceme předpovědět)
- **xᵢⱼ** = hodnoty vysvětlujících proměnných (regresory, prediktory)
- **β₀** = konstanta (intercept) - hodnota Y, když všechny X = 0
- **β₁, β₂, ...** = regresní koeficienty (jak moc X ovlivňuje Y)
- **εᵢ** = náhodná chyba (co model nedokáže vysvětlit)
- **i** = index pozorování (1, 2, 3, ..., n)

### Maticový zápis (pro všechna pozorování najednou)
```
y = Xβ + ε
```

**Datová matice X** (n × (k+1)):
- n řádků = n pozorování
- k+1 sloupců = 1 konstanta + k vysvětlujících proměnných

---

## 2. PŘEDPOKLADY MODELU

Pro správné fungování lineární regrese musí platit:

### ✓ 1. Střední hodnota chyby je nulová
```
E(ε) = 0
```
Chyby se v průměru "vyruší".

### ✓ 2. Konstantní rozptyl (homoskedasticita)
```
var(ε) = σ²
```
Rozptyl chyb je stejný pro všechna pozorování.

### ✓ 3. Chyby jsou nekorelované
```
cov(εᵢ, εⱼ) = 0  pro i ≠ j
```
Chyba v jednom pozorování neovlivňuje chybu v jiném.

### ✓ 4. Nezávislé proměnné nejsou náhodné
X je matice konstantních hodnot (ne náhodných).

### ✓ 5. Lineární nezávislost
Sloupce matice X nesmí být lineárně závislé (žádná proměnná není dokonalá kombinace jiných).

### ✓ 6. Normalita (pro testy)
```
ε ~ N(0, σ²)
```
Chyby mají normální rozdělení (potřebné pro t-testy a F-testy).

---

## 3. METODA NEJMENŠÍCH ČTVERCŮ (OLS)

### Cíl
Najít koeficienty **β**, které **minimalizují součet čtverců chyb** (RSS):

```
RSS = Σ(yᵢ - ŷᵢ)² = (y - Xb)ᵀ(y - Xb)
```

kde:
- **ŷᵢ** = předpovězená hodnota z modelu
- **yᵢ - ŷᵢ** = reziduum (rozdíl mezi skutečnou a předpovězenou hodnotou)

### Řešení

**Normální rovnice:**
```
XᵀXb = Xᵀy
```

**Explicitní vzorec pro odhady:**
```
b = (XᵀX)⁻¹Xᵀy
```

**Vlastnosti odhadů:**
- ✅ **Nestranné**: E(b) = β
- ✅ **BLU** (Best Linear Unbiased): nejlepší lineární nestranné odhady
- ✅ **Kovariační matice**: cov(b) = σ²(XᵀX)⁻¹

---

## 4. VÝSTUP Z REGRESE - JAK ČÍST TABULKU

### A) Tabulka koeficientů

| Proměnná | Koeficient | SE | t-statistika | p-hodnota |
|----------|------------|-----|--------------|-----------|
| Konstanta | b₀ | s(b₀) | t₀ | p₀ |
| x₁ | b₁ | s(b₁) | t₁ | p₁ |
| x₂ | b₂ | s(b₂) | t₂ | p₂ |

**Význam:**
- **Koeficient (b)**: O kolik se změní Y, když X vzroste o 1 (při fixních ostatních X)
- **SE (standard error)**: Směrodatná chyba odhadu = míra nejistoty
- **t-statistika**: t = koeficient / SE
- **p-hodnota**: Pravděpodobnost, že by takový koeficient vznikl náhodou
  - p < 0,05 → statisticky významný ✓
  - p ≥ 0,05 → není statisticky významný ✗

### B) ANOVA tabulka (Analýza rozptylu)

| Zdroj | DF | Sum of Squares | Mean Square | F | p-value |
|-------|-----|----------------|-------------|---|---------|
| Model | k | MSS | MSS/k | F | p |
| Error | n-k-1 | RSS | RSS/(n-k-1) = s² | | |
| Total | n-1 | TSS | | | |

**Význam:**
- **MSS** (Model Sum of Squares) = variabilita vysvětlená modelem
- **RSS** (Residual Sum of Squares) = nevysvětlená variabilita
- **TSS** (Total Sum of Squares) = celková variabilita
- **F-statistika**: testuje, zda má model jako celek smysl
  - F = (MSS/k) / (RSS/(n-k-1))
  - p < 0,05 → model JE významný ✓

### C) Index determinace (R²)

```
R² = MSS/TSS = 1 - RSS/TSS
```

**Interpretace:**
- R² = 0,75 → **Model vysvětluje 75% variability**
- R² ∈ [0, 1]
  - R² = 1 → dokonalé vysvětlení
  - R² = 0 → model nevysvětluje nic

**Adjustovaný R²** (lépe pro porovnávání modelů):
```
R²ₐdⱼ = 1 - (RSS/(n-k-1))/(TSS/(n-1))
```
Penalizuje za každou další přidanou proměnnou.

### D) Směrodatná odchylka residuí

```
s = √(RSS/(n-k-1))
```

**Interpretace:** Průměrná velikost chyby modelu (v jednotkách Y).

---

## 5. TESTOVÁNÍ HYPOTÉZ

### Test jednotlivého koeficientu

**Hypotézy:**
- H₀: βᵢ = 0 (proměnná NEMÁ vliv)
- H₁: βᵢ ≠ 0 (proměnná MÁ vliv)

**Testová statistika:**
```
t = bᵢ / s(bᵢ)  ~  t(n-k-1)
```

**Kritická hodnota:**
- Pro α = 0,05 a df = n-k-1, najdeme v t-tabulce
- Např. df = 30 → t₀.₀₂₅(30) = 2,042

**Rozhodnutí:**
- |t| > kritická hodnota → **ZAMÍTÁME H₀** (koeficient je významný) ✓
- |t| < kritická hodnota → nezamítáme H₀

### Test celého modelu (F-test)

**Hypotézy:**
- H₀: β₁ = β₂ = ... = βₖ = 0 (žádná proměnná nemá vliv)
- H₁: alespoň jeden βⱼ ≠ 0

**Testová statistika:**
```
F = (MSS/k) / (RSS/(n-k-1))  ~  F(k, n-k-1)
```

**Rozhodnutí:**
- F > kritická hodnota → model JE významný ✓

---

## 6. INTERVALOVÝ ODHAD KOEFICIENTU

**95% interval spolehlivosti pro βᵢ:**

```
bᵢ ± t₀.₀₂₅(n-k-1) × s(bᵢ)
```

**Příklad:**
- bᵢ = 0,0921
- s(bᵢ) = 0,0109
- t₀.₀₂₅(30) = 2,042

```
IS = 0,0921 ± 2,042 × 0,0109
IS = 0,0921 ± 0,0223
IS = [0,0698 ; 0,1144]
```

**Interpretace:** S 95% jistotou leží skutečná hodnota βᵢ v intervalu [0,0698 ; 0,1144].

---

## 7. REGRESNÍ DIAGNOSTIKA

### A) Residua (rezidua)

**Residuum** = rozdíl mezi pozorovanou a předpovězenou hodnotou:
```
eᵢ = yᵢ - ŷᵢ
```

**Typy residuí:**

1. **Klasická residua**: eᵢ
2. **Normovaná**: eᵢ/s
3. **Standardizovaná**: eᵢ/(s√(1-hᵢᵢ))
4. **Studentizovaná**: eᵢ/(s₍₋ᵢ₎√(1-hᵢᵢ))

### B) Ověření předpokladů

**1. Normalita residuí:**
- QQ-graf (kvantil-kvantil)
- Shapiro-Wilk test
- Histogr residuí

**2. Konstantní rozptyl (homoskedasticita):**
- Graf residuí vs. předpovězené hodnoty
- Měl by být "náhodný oblak" bodů

**3. Autokorelace (nekorelovanost residuí):**
```
Durbin-Watson statistika: DW ≃ 2(1 - ρ̂)
```
- DW ≈ 2 → žádná autokorelace ✓
- DW < 2 → pozitivní autokorelace
- DW > 2 → negativní autokorelace

### C) Vlivné body

**Leverage (páka):**
- hᵢᵢ = diagonální prvky projekční matice H
- hᵢᵢ > 2(k+1)/n → vlivný bod

**Cookova vzdálenost:**
```
Cᵢ = (hᵢᵢ/(k+1(1-hᵢᵢ))) × e²ₛᵢ
```
- Cᵢ ≥ 1 → velmi vlivný bod (zvažte odstranění)

---

## 8. PRAKTICKÝ PŘÍKLAD

### Data
```
Y (spotřeba) = β₀ + β₁×(pracovní_dny) + β₂×(teplota) + ε
```

### Výstup

**Koeficienty:**

| Proměnná | Koeficient | SE | t | p |
|----------|-----------:|----:|----:|----:|
| Konstanta | 13,62 | 0,85 | 16,0 | 0,000 |
| Pracovní dny | -0,22 | 0,04 | -5,5 | 0,001 |
| Teplota | -0,08 | 0,01 | -8,0 | 0,000 |

**ANOVA:**

| Zdroj | DF | SS | MS | F | p |
|-------|----:|------:|------:|------:|------:|
| Model | 2 | 89,2 | 44,6 | 46,9 | 0,000 |
| Error | 10 | 9,5 | 0,95 | | |
| Total | 12 | 98,7 | | | |

**R² = 0,904** → Model vysvětluje 90,4% variability

### Interpretace

1. **Konstanta (13,62)**: Když pracovní dny = 0 a teplota = 0, spotřeba = 13,62
2. **Pracovní dny (-0,22)**: Každý další pracovní den SNÍŽÍ spotřebu o 0,22
3. **Teplota (-0,08)**: Každý stupeň SNÍŽÍ spotřebu o 0,08
4. **Všechny koeficienty jsou významné** (p < 0,05)
5. **Model jako celek je významný** (F-test: p < 0,05)

---

## 9. SHRNUTÍ - CO POTŘEBUJU VĚDĚT

### ✅ Model
```
y = Xβ + ε
```

### ✅ Odhad
```
b = (XᵀX)⁻¹Xᵀy
```

### ✅ Testování koeficientu
```
t = b/SE  ~  t(n-k-1)
|t| > t_kritická → významný ✓
```

### ✅ Kvalita modelu
```
R² = MSS/TSS  (0 až 1)
F = MS_model / MS_error
```

### ✅ Co kontrolovat
- p-hodnoty koeficientů (< 0,05 ✓)
- p-hodnotu F-testu (< 0,05 ✓)
- R² (čím vyšší, tím lepší)
- Normalitu residuí (QQ-graf)
- Konstantní rozptyl (graf residuí)
- Vlivné body (Cookova vzdálenost)

---

## 10. ČASTÉ OTÁZKY

### Q: Co když p-hodnota > 0,05?
**A:** Proměnná není statisticky významná → zvažte její odstranění z modelu.

### Q: Co když R² je nízké?
**A:** Model špatně vysvětluje data → chybí důležité proměnné nebo vztah není lineární.

### Q: Jak velké R² je dobré?
**A:** Záleží na oboru:
- Fyzika/technika: R² > 0,9
- Sociální vědy: R² > 0,5 může být dobré
- Biologie: R² > 0,7

### Q: Co dělat s multikolinearitou?
**A:** Když proměnné jsou příliš korelované:
- Odstraňte jednu z korelovaných proměnných
- Použijte PCA (analýzu hlavních komponent)
- Ridge/Lasso regresi

### Q: Kolik pozorování potřebuju?
**A:** Pravidlo palce: **n ≥ 10 × (k+1)**
- Pro 3 proměnné: n ≥ 40
- Čím víc, tím lépe!

---

## SLOVNÍČEK POJMŮ

| Pojem | Význam |
|-------|--------|
| **Regresor** | Vysvětlující proměnná (X) |
| **Závislá proměnná** | To, co předpovídáme (Y) |
| **Reziduum** | Rozdíl mezi pozorovanou a předpovězenou hodnotou |
| **RSS** | Residual Sum of Squares = suma čtverců residuí |
| **MSS** | Model Sum of Squares = vysvětlená variabilita |
| **TSS** | Total Sum of Squares = celková variabilita |
| **OLS** | Ordinary Least Squares = metoda nejmenších čtverců |
| **SE** | Standard Error = směrodatná chyba |
| **DF** | Degrees of Freedom = stupně volnosti |
| **Homoskedasticita** | Konstantní rozptyl chyb |
| **Heteroskedasticita** | Nekonstantní rozptyl chyb |
| **Multikolinearita** | Vysoká korelace mezi regresory |

---

**Hodně štěstí se studiem! 📊📈**
