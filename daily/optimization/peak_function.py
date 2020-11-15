import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# init variables
x1 = sp.Symbol('x1')
x2 = sp.Symbol('x2')
# init "peak" function
y = 3 * ((1 - x1) ** 2) * (sp.E ** (-x1 ** 2 - (x2 + 1) ** 2)) - 10 * (x1 / 5 - x1 ** 3 - x2 ** 5) * (
        sp.E ** (-x1 ** 2 - x2 ** 2)) - sp.E ** (-(x1 + 1) ** 2 - x2 ** 2) / 3
X = np.zeros((2, 1))  # X = np.ones((2, 1)), X = np.ones((2, 1))*2
g_X = np.array(
    [[y.diff(x1).evalf(subs={x1: X[0][0], x2: X[1][0]})], [y.diff(x2).evalf(subs={x1: X[0][0], x2: X[1][0]})]])
# SD for "peak" function
step = 0
Y = [np.dot(g_X.T, g_X).sum() ** 0.5]
while np.dot(g_X.T, g_X).sum() ** 0.5 > 10 ** -5:
    r = g_X
    H = np.array(
        [[y.diff(x1, x1).evalf(subs={x1: X[0][0], x2: X[1][0]}), y.diff(x1, x2).evalf(subs={x1: X[0][0], x2: X[1][0]})],
         [y.diff(x2, x1).evalf(subs={x1: X[0][0], x2: X[1][0]}),
          y.diff(x2, x2).evalf(subs={x1: X[0][0], x2: X[1][0]})]])
    a = np.dot(r.T, r) / np.dot(r.T, H.dot(r))
    X = X - a * r
    step += 1
    g_X = np.array(
        [[y.diff(x1).evalf(subs={x1: X[0][0], x2: X[1][0]})], [y.diff(x2).evalf(subs={x1: X[0][0], x2: X[1][0]})]])
    Y.append(np.dot(g_X.T, g_X).sum() ** 0.5)
# visual
plt.plot([i for i in range(0, step + 1)], Y, "r-", label="peak function")
plt.title("Error Curve")
plt.xlabel("step")
plt.ylabel("2-norm")
plt.show()
