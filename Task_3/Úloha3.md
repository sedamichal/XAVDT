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
4. $h(\times{X}) = k + 1 \leq n$ &emsp;>> sloupce matice $\textbf{X}$ nejsou lineárně závislé a počet pozorování je alespoň roven počtu parametrů

## Odvoďte vztahy pro odhad parametrů modelu metodou nejmenších čtverců

## Co je to projekční matice? Jaké má rozměry? Co znamenají hodnoty jejich diagonálních prvků?
