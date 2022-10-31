import numpy as np


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)


def function_1(x):
    return 0.01*x**2 + 0.1*x


print(numerical_diff(function_1, 5))
print(numerical_diff(function_1, 10))

