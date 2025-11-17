
$$
a = [1,1,1]^T
$$
$$
x = [x_1,x_2,x_3]^T
$$
$$
B = \begin{bmatrix}
   1 & -2 & 3 \\
   -2 & 3 & 3 \\
   3 & 3 & 2
\end{bmatrix}
$$
---
## a. **$a^Tx$**
$$
a^Tx = \begin{bmatrix}1 & 1 & 1\end{bmatrix} \begin{bmatrix}x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_1 + x_2 + x_3
$$
---
## b. **$ax^T$**
$$
ax^T = \begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix}\begin{bmatrix}x_1 & x_2 & x_3\end{bmatrix}=\begin{bmatrix}x_1 & x_2 & x_3 \\ x_1 & x_2 & x_3 \\ x_1 & x_2 & x_3\end{bmatrix}
$$
---
## c. **$Ba$**
$$
Ba = \begin{bmatrix}
   1 & -2 & 3 \\
   -2 & 3 & 3 \\
   3 & 3 & 2\end{bmatrix}\begin{bmatrix}1 \\ 1 \\ 1 \end{bmatrix}=\begin{bmatrix}2 \\ 4 \\ 8 \end{bmatrix}
$$
---
## d. $\dfrac{\partial x^T B x}{\partial x}$

$$
x^T B x = \begin{bmatrix}x_1 & x_2 & x_3\end{bmatrix}\begin{bmatrix}1 & -2 & 3 \\
   -2 & 3 & 3 \\
   3 & 3 & 2\end{bmatrix}\begin{bmatrix}x_1 \\ x_2 \\ x_3\end{bmatrix}
$$
$$
x^T B = \begin{bmatrix}x_1 & x_2 & x_3\end{bmatrix}\begin{bmatrix}1 & -2 & 3 \\
   -2 & 3 & 3 \\
   3 & 3 & 2\end{bmatrix}=
   \begin{bmatrix}
   x_1-2x_2+3x_3 & -2x_1+3x_2+3x_3 & 3x_1+3x_2+2x_3
   \end{bmatrix}
$$
$$
x^T B x = (x_1 - 2x_2 + 3x_3)x_1 + (-2x_1+3x_2+3x_3)x_2 + (3x_1+3x_2+2x_3)x_3 = x_1^2 - 2x_1x_2 + 3x_1x_3 -2x_1x_2 + 3x_2^2 + 3x_2x_3 + 3x_1x_3 +3x_2x_3 + 2x_3^2
$$
$$
x^T B x = x_1^2 - 4x_1x_2 + 6x_1x_3 + 3x_2^2 + 6x_2x_3 + 2x_3^2
$$
$$
\dfrac{\partial}{\partial x_1}( x^T B x) = 2x_1 - 4x_2 + 6x_3 
$$
$$
\dfrac{\partial}{\partial x_2}( x^T B x) = -4x_1 + 6x_2 + 6x_3
$$
$$
\dfrac{\partial}{\partial x_3}( x^T B x) = 6x_1 + 6x_2 + 4x_3 
$$

**$$
\dfrac{\partial x^T B x}{\partial x} = 
\begin{bmatrix}
2x_1 - 4x_2 + 6x_3 \\
-4x_1 + 6x_2 + 6x_3 \\
6x_1 + 6x_2 + 4x_3
\end{bmatrix}
$$**