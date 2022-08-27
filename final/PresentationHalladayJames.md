
Section 6.3.1: Multi-Dimensional Gradient Descent
========================================================
author: James Halladay
date: 11/16/21
autosize: true


 
What is a Gradient?
========================================================
Differentiation can be generalized to multiple dimensions in the form of a gradient.

Taking the gradient of a function returns a vector containing every partial derivative  of a function.

$$
  \nabla f(x_1, x_2, \ldots, x_n) = \begin{bmatrix}
  \frac{\partial f}{\partial x_1} \\
  \frac{\partial f}{\partial x_2} \\
  \vdots \\
  \frac{\partial f}{\partial x_n}
  \end{bmatrix}
$$


Gradient Descent
========================================================
Gradient Descent is the process of using the gradient of a differentiable function to find a local minimum of the function from an initial point.

Starting from the initial value, the gradient is evaluated at that value. We then step down the curve of the gradient to find a new value until the value converges to a local minimum of the function, meaning the gradient is approximately equal to 0.

<text> </text>








```
Error in mesh(seq(-2, 2, length.out = 50), seq(-5, 5, length.out = 50)) : 
  could not find function "mesh"
```
