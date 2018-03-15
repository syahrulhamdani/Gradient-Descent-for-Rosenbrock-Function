# Gradient Descent for Rosenbrock Function

This is python code for implementing **Gradient Descent** to find minima of Rosenbrock Function.
Rosenbrock function is a non-convex function, introducesd by Howard H. Rosenbrock in 1960, which is mostly used for performance test problem for optimization algorithm.

If you want to know more about the function, you can find its wiki [here](https://en.wikipedia.org/wiki/Rosenbrock_function). If you are so curious about Gradient Descent too, you can find a good reading [right here](http://ruder.io/optimizing-gradient-descent/).


## Test Case

For this example, I decide to perform 2 cases:
1. Setting `a` and `b` equals `0` and `100` respectively
2. Setting `a` and `b` equals `1` and `100` respectively

The reason is because I want to compare using gradient descent for trivial (1st case) and non trivial (2nd case).

## How to Use

Inside the code, I have included some comments so that you can choose whether you want to use 1st or 2nd case. Just follow what the comment says.

### Notes

This is just simple Gradient Descent. Further, the learning rate can be improved by changing it for every different points.