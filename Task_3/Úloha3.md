## Zapište maticově lineární regresní model, uveďte rozměry jednotlivých matic a vektorů

$$
  \textbf{y} = \textbf{X} \beta + \epsilon
$$

pro řádek

$$
y_i = \textbf{x}^T_i \beta + \epsilon_i
$$

### rozměry matic a vektorů

$$\textbf{y}_n$$
---
$n$ je počet pozorovaných hodnot


$$X_{n\times{(k+1)}}$$
---
$n$ je počet pozorovaných hodnot

$k$ je počet paramterů modelu

$$\epsilon_n$$
---
$n$ je počet pozorovaných hodnot

## Jaké jsou předpoklady v klasickém lineárním modelu?
1. $E(\epsilon) = 0$
2. $cov(\epsilon) = \sigma^2 \textbf{I}_n, \sigma^2>0$ &emsp;>> náhodné složky jsou nekorelované
3. $\textbf{X}$ je nenáhodná matice $n \times{(k+1)}$
4. hodnost matice $h(X) = k + 1 \leq n$ &emsp;>> sloupce matice $\textbf{X}$ nejsou lineárně závislé a počet pozorování je alespoň roven počtu parametrů

## Odvoďte vztahy pro odhad parametrů modelu metodou nejmenších čtverců
Reziduální suma čtverců:
$$
RSS=(y-Xb)^T(y-Xb) = y^Ty - y^TXb - (Xb)^Ty + (Xb)^T(Xb) = y^Ty - y^TXb - b^TX^Ty + b^TX^TXb = y^Ty - 2b^TX^Ty + b^TX^TXb
$$
Minimalizace RSS
- Derivace podle vektoru $b$
$$
\dfrac{\partial RSS}{\partial b} = \dfrac{\partial (y^Ty - 2b^TX^Ty + b^TX^TXb) }{\partial b} = -2X^Ty+2X^TXb
$$
- Derivace rovna nulovému vektoru
$$
-2X^Ty+2X^TXb = 0
$$
$$
X^Ty = X^TXb
$$
Vztah pro odhad parametrů
$$
b = (X^TX)^{-1}X^Ty
$$

## Co je to projekční matice? Jaké má rozměry? Co znamenají hodnoty jejich diagonálních prvků?
1. Matice projekce se používá k nalezení **odhadovaných hodnot** závislé proměnné. Mějme matici regresorů $X$ a vektor $y$. Projekční matice $H$ promítá vektor $\boldsymbol{y}$ do **sloupcového prostoru** matice $X$
$$
\hat{y} = Xb = X(X^TX)^{-1}X^Ty = Hy
$$

2. Rozměry projekční matice jsou $N \times N$

|Matice|Rozměr|
|------|------|
|$X$|$N \times K$|
|$X^T$|$K \times N$|
|$X^TX$|$K \times K$|
|$(X^TX)^{−1}$|$K \times K$|
|$H=X(X^TX)^{−1}X^T$|$(N \times K)⋅(K \times K)⋅(K \times N)→ N \times N$|

3. Hodnoty diagonálních prvků projekční matice představují pákový efekt $i$-tého pozorování. Hodnota je úměrná vzdálenosti $i$-tého prvku od těžiště, je považováná za velkou, pokud je větší než dvojnásobek průměrné hodnoty $h_{ij} > 2(k+1)/n$
