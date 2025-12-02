Regression Equation Section
|Independent Variable|Regression Coefficient b(i)|Standard Error Sb(i)|
|---|---|---|
|Intercept|15.814|0.748|
|x1|-1.015|0.063|
|x2|0.065|0.003|

Analysis of Variance Section
|Source|DF|Sum of Squares|Mean Square|F-Ratio|Prob|Level|
|---|---|---|---|---|---|---|
|Model|2|102.77|51.38|207.6|0.0000|
|Error|12|2.97|0.247|

## Napište tvar regresního modelu pro tento příklad

Tvar regresního modelu se skládá z koeficientů (sloupec $b(i)$) pro **Intercept** a **nezávislé proměnné** ($x_1, x_2$).
    Regresní rovnice:$$\hat{y} = 15.814 - 1.015 x_1 + 0.065 x_2$$
    
Interpretace koeficientů:

- **Intercept** ($b_0 = 15.814$):<br>Očekávaná hodnota závislé proměnné ($\hat{y}$), pokud jsou obě nezávislé proměnné ($x_1$ a $x_2$) rovny nule.
    
- **$x_1$** ($b_1 = -1.015$):<br>Zvýšení $x_1$ o jednu jednotku vede ke snížení $\hat{y}$ o $1.015$ jednotek, za předpokladu, že $x_2$ zůstane konstantní (ceteris paribus).

- **$x_2$** ($b_2 = 0.065$):<br>Zvýšení $x_2$ o jednu jednotku vede ke zvýšení $\hat{y}$ o $0.065$ jednotek, za předpokladu, že $x_1$ zůstane konstantní (ceteris paribus).

## Jaký byl rozsah výběru (kolik řádků v datové matici)?

Rozsah výběru ($N$) se vypočítá pomocí stupňů volnosti (DF) z tabulky ANOVA.
DF pro Model je $k = 2$ (počet nezávislých proměnných $x_1, x_2$).DF pro Error (rezidua) je $N - k - 1 = 12$.Dosazením a řešením pro $N$:$$N - 2 - 1 = 12$$$$N - 3 = 12$$$$N = 15$$Rozsah výběru (počet řádků): $N = 15$

## Lze zamítnout některou z hypotéz, že regresní koeficienty jsou nulové?

K ověření, zda lze zamítnout hypotézu, že daný regresní koeficient ($\beta_i$) je nulový ($H_0: \beta_i = 0$), se používá **$t-test$**.

**Testování celého modelu (F-test):**<br>
F-Ratio: $207.6$<br>
Prob Level (p-hodnota): $0.0000$

Protože je $p$-hodnota ($0.0000$) menší než jakákoli obvyklá hladina významnosti ($\alpha=0.05$ nebo $\alpha=0.01$), zamítáme nulovou hypotézu, že všechny regresní koeficienty ($x_1, x_2$) jsou nulové. Model je jako celek statisticky vysoce významný.

**Testování jednotlivých koeficientů (t-test):**<br>
Hodnoty $t$-statistiky se počítají jako poměr koeficientu k jeho standardní chybě: $t_i = b_i / S_{b_i}$.

|Koeficient|b(i)|Sb(i)|​t-statistika|Interpretace|
|---|---|---|---|---|
|Intercept|15.814|0.748|21.1417|Zamítáme $H_0$|
|$x_1$|-1.015|0.063|-16.1111|Zamítáme $H_0$|
|$x_2$|0.065|0.003|21.6667|Zamítáme $H_0$|

**Výpočet t-statistiky:**<br>
$$t_{\text{Intercept}} = 15.814 / 0.748 \approx 21.1417$$

$$t_{x_1} = -1.015 / 0.063 \approx -16.1111$$
$$t_{x_2} = 0.065 / 0.003 \approx 21.6667$$

Stupně volnosti (DF Error) pro $t$-test jsou $12$:<br>
Kritická hodnota $t$ pro oboustranný test při $\alpha=0.05$ a $12$ DF je $2.179$:<br>
.

Protože jsou absolutní hodnoty všech $t$-statistik (včetně interceptu) větší než $2.179$, lze zamítnout nulovou hypotézu, že daný regresní koeficient je nulový, pro všechny koeficienty (Intercept, $x_1$ a $x_2$).

## Spočítejte hodnotu indexu determinace


## Statistický kontext
Princip testování nulovosti regresního koeficientu pomocí $t$-testu je založen na následujícím:

Hypotéza ($H_0$):<br>
Nulová hypotéza tvrdí, že regresní koeficient ($\beta_i$) je roven nule ($H_0: \beta_i = 0$). To by znamenalo, že nezávislá proměnná ($x_i$) nemá žádný lineární vliv na závisle proměnnou ($y$) v populaci.

Testová statistika ($t$):<br>
Pro testování této hypotézy se používá $t$-statistika, která se vypočítá jako:$$t = \frac{b_i}{S_{b_i}}$$<br>
Kde $b_i$ je odhadnutý koeficient (z výstupu regrese) a $S_{b_i}$ je jeho standardní chyba.

Rozhodnutí:<br>
Tato vypočtená $t$-hodnota se porovná s kritickou hodnotou $t$ (při dané hladině významnosti $\alpha$ a příslušném počtu stupňů volnosti) nebo se použije $p$-hodnota (která často bývá uvedena v plném výstupu regrese). Pokud je absolutní hodnota $t$-statistiky vysoká (nebo $p$-hodnota nízká, typicky menší než $0.05$), nulovou hypotézu zamítáme.