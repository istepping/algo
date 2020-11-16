import sympy as sp
import matplotlib.pyplot as plt
import numpy as np


# 计算向量的二范数
def calc_two_norm(d_k):
    two_norm = (np.dot(d_k.T, d_k).sum()) ** 0.5
    return two_norm


def calc_gradient(var):
    x_k = var[0][0]
    y_k = var[1][0]
    pd_x = f_x_y.diff(x).evalf(subs={x: x_k, y: y_k})
    pd_y = f_x_y.diff(y).evalf(subs={x: x_k, y: y_k})
    return np.array([[pd_x], [pd_y]])


def calc_hessian(var):
    x_k = var[0][0]
    y_k = var[1][0]
    pd_x_x = f_x_y.diff(x, x).evalf(subs={x: x_k, y: y_k})
    pd_x_y = f_x_y.diff(x, y).evalf(subs={x: x_k, y: y_k})
    pd_y_y = f_x_y.diff(y, y).evalf(subs={x: x_k, y: y_k})
    pd_y_x = f_x_y.diff(y, x).evalf(subs={x: x_k, y: y_k})
    return np.array([[pd_x_x, pd_x_y], [pd_y_x, pd_y_y]])


def calc_alpha(g_k, H_k):
    numerator = np.dot(g_k.T, g_k)
    denominator = np.dot(np.dot(g_k.T, H_k), g_k)
    return numerator / denominator


if __name__ == '__main__':
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    f_x_y = 3 * ((1 - x) ** 2) * (sp.E ** (-x ** 2 - (y + 1) ** 2)) - 10 * (x / 5 - x ** 3 - y ** 5) * (
            sp.E ** (-x ** 2 - y ** 2)) - sp.E ** (-(x + 1) ** 2 - y ** 2) / 3

    variable = np.array([[-1], [-1]])
    print("x:\n", variable, "\n")
    gradient = calc_gradient(variable)
    two_norm = calc_two_norm(gradient)
    print("2-norm of derivative:\n", two_norm, "\n")

    iter_count = 1
    two_norm_list = [two_norm]
    while two_norm > 1e-5:
        print("-" * 50)

        iter_count += 1

        hessian = calc_hessian(variable)

        alpha = calc_alpha(gradient, hessian)

        variable = variable - alpha * gradient
        print("x:\n", variable, "\n")

        gradient = calc_gradient(variable)
        two_norm = calc_two_norm(gradient)
        two_norm_list.append(two_norm)
        print("2-norm of derivative:\n", two_norm, "\n")

    print("maximum:\n", variable, "\n")
    plt.plot([x for x in range(iter_count)], two_norm_list)
    plt.show()
