# Přehled parametrů Wine datasetu

## Zdroj dat
**UCI Machine Learning Repository - Wine Recognition Data**  
https://archive.ics.uci.edu/ml/datasets/wine

**Dataset:** 178 vzorků vín ze 3 odrůd révy vinné z Itálie  
**Proměnné:** 13 chemických parametrů

---

## 1. ALCOHOL (Alkohol)
- **Jednotka:** % obj.
- **Popis:** Obsah ethanolu ve víně. Vyšší hodnoty = silnější víno. Ovlivňuje chuť, tělo a stabilitu.
- **Interpretace:** ↑ = silnější víno, vyšší extraktivita
- **Typický rozsah:** 11-15%

## 2. MALIC ACID (Kyselina jablečná)
- **Jednotka:** g/L
- **Popis:** Hlavní organická kyselina v hroznech. Ovlivňuje kyselost a čerstvost vína. Klesá při dozrávání hroznů.
- **Interpretace:** ↑ = kyselejší, čerstvější víno
- **Poznámka:** Během malolaktické fermentace se přeměňuje na kyselinu mléčnou

## 3. ASH (Popel)
- **Jednotka:** g/L
- **Popis:** Anorganické minerály zbylé po spálení vína. Indikátor minerálního složení půdy.
- **Interpretace:** ↑ = vyšší minerální obsah
- **Obsahuje:** K, Ca, Mg, Na, Fe a další minerály

## 4. ALCALINITY OF ASH (Alkalinita popela)
- **Jednotka:** meq/L (miliekvivalenty na litr)
- **Popis:** Schopnost popela neutralizovat kyseliny. Souvisí s obsahem draslíku, vápníku a hořčíku.
- **Interpretace:** ↑ = vyšší pH, nižší kyselost
- **Souvisí s:** Pufrační kapacitou vína

## 5. MAGNESIUM (Hořčík)
- **Jednotka:** mg/L
- **Popis:** Důležitý minerál z půdy. Ovlivňuje enzymatické reakce při fermentaci. Indikátor terroir.
- **Interpretace:** ↑ = bohatší půda, lepší terroir
- **Rozsah:** 70-162 mg/L v datasetu

## 6. TOTAL PHENOLS (Celkové fenoly)
- **Jednotka:** g/L
- **Popis:** Suma všech fenolických sloučenin. Antioxidanty, ovlivňují barvu, chuť a stárnutí vína.
- **Interpretace:** ↑ = větší antioxidační kapacita
- **Zahrnuje:** Flavonoidy + neflavonoidní fenoly
- **Význam:** Nejvyšší u červených vín

## 7. FLAVANOIDS (Flavonoidy)
- **Jednotka:** g/L
- **Popis:** Podskupina fenolů. Hlavní antioxidanty, ovlivňují barvu (červená), chuť (trpkost) a zdravotní přínosy.
- **Interpretace:** ↑ = silnější barva, více tříslovin
- **Zahrnuje:** Katechiny, anthokyaniny, quercetin
- **⭐ KLÍČOVÝ PARAMETR pro rozlišení odrůd!**

## 8. NONFLAVANOID PHENOLS (Neflavonoidní fenoly)
- **Jednotka:** g/L
- **Popis:** Fenoly bez flavonoidní struktury. Menší vliv na barvu, ale přispívají k celkové chuti.
- **Interpretace:** ↓ = čistší flavonoidní profil
- **Zahrnuje:** Kyselina gallová, kyselina kávová, tyrosol

## 9. PROANTHOCYANINS (Proanthokyaniny)
- **Jednotka:** mg/L
- **Popis:** Typ flavonoidů (kondenzované taniny). Zodpovědné za trpkost a "tělnatost" červených vín. Stabilizují barvu.
- **Interpretace:** ↑ = trpčí, tělnatější víno
- **Pocit:** "Sucho" v ústech po červeném víně

## 10. COLOR INTENSITY (Intenzita barvy)
- **Jednotka:** bezrozměrná (absorbance)
- **Popis:** Měří intenzitu/sytost barvy vína. Vyšší u červených vín, nižší u bílých.
- **Interpretace:** ↑ = tmavší, sytější barva
- **Měření:** Spektrofotometricky

## 11. HUE (Odstín)
- **Jednotka:** bezrozměrná (poměr absorbancí)
- **Popis:** Odstín/tón barvy. 
  - Nízké hodnoty = červená/fialová (mladá vína)
  - Vysoké hodnoty = oranžová/hnědá (oxidace, stárnutí)
- **Interpretace:** ↓ = mladší, ↑ = starší/oxidované
- **Výpočet:** OD420/OD520

## 12. OD280/OD315 OF DILUTED WINES (OD280/OD315 zředěných vín)
- **Jednotka:** poměr (bezrozměrný)
- **Popis:** Poměr absorbancí UV světla při 280 nm a 315 nm. Indikátor obsahu proteinů a fenolů.
- **Interpretace:** ↑ = vyšší kvalita, více proteinů a fenolů
- **Proč zředěné?** Čisté víno je příliš tmavé pro přesné měření
- **OD280:** Zachycuje proteiny + fenoly
- **OD315:** Zachycuje flavonoidy + barevné látky
- **⭐ RYCHLÝ TEST kvality vína!**

## 13. PROLINE (Prolin)
- **Jednotka:** mg/L
- **Popis:** Aminokyselina. Nejvíce zastoupená aminokyselina ve víně (až 85%). Ovlivňuje nutriční hodnotu a chuť.
- **Interpretace:** ↑ = nutriční hodnota, plnost
- **Rozsah:** 278-1680 mg/L v datasetu (obrovská variabilita!)
- **Zajímavost:** Některé odrůdy mají 10× vyšší obsah než jiné

---

## Skupiny parametrů

### 1. ZÁKLADNÍ SLOŽENÍ
- **Alcohol** - hlavní alkohol
- **Malic acid** - hlavní kyselina
- **Ash, Alcalinity, Magnesium** - minerální složení (terroir)

### 2. FENOLICKÉ SLOUČENINY
*(Antioxidanty, barva, chuť)*
- **Total phenols** - celkový obsah fenolů
- **Flavanoids** - hlavní barevné a tříslovinové látky ⭐
- **Nonflavanoid phenols** - doplňkové fenoly
- **Proanthocyanins** - třísloviny (trpkost)

### 3. OPTICKÉ VLASTNOSTI
- **Color intensity** - síla barvy
- **Hue** - odstín barvy (mladé vs. staré)
- **OD280/OD315** - spektrofotometrický ukazatel kvality ⭐

### 4. AMINOKYSELINY
- **Proline** - hlavní aminokyselina

---

## Klíčové poznatky z PCA

**Nejdůležitější parametry pro rozlišení odrůd (PC1):**
1. **Flavanoids** (0,92) ⭐⭐⭐
2. **Total phenols** (0,86) ⭐⭐
3. **OD280/OD315** (0,82) ⭐⭐
4. **Proanthocyanins** (0,68) ⭐

→ **Fenolické sloučeniny jsou hlavním faktorem variability!**

---

## Praktické využití

### Pro vinaře:
- **Flavonoidy + Total phenols** → kvalita, potenciál stárnutí
- **Malic acid** → čerstvost, vhodnost pro malolaktickou fermentaci
- **Proline** → typické pro určité odrůdy
- **Hue** → monitorování oxidace/stárnutí

### Pro analytiky:
- **OD280/OD315** → rychlý test kvality (nemusíte měřit všechny fenoly samostatně)
- **Magnesium + Alkalinita** → "otisk prstu" půdy/terroir
- **Color intensity + Hue** → vizuální kvalita

### Pro spotřebitele:
- **Alcohol** → síla vína
- **Proanthocyanins** → trpkost červených vín
- **Total phenols** → antioxidační přínosy

---

## Reference
- Forina, M. et al. (1991). PARVUS - An Extendible Package for Data Exploration
- UCI Machine Learning Repository (2019)
- Jackson, R.S. (2008). Wine Science: Principles and Applications
