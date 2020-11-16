import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_spd_matrix


# 生成随机的二次项系数:nxn矩阵
def create_A(n_dim: int):
    return make_spd_matrix(n_dim)


# 生成随机的一次项系数:nx1矩阵
def create_b(n_dim: int):
    return np.random.rand(n_dim, 1)


# 计算一阶导数:Ax-b
def calc_first_order(A, b, x_k):
    return np.dot(A, x_k) - b


# 计算向量的二范数
def calc_two_norm(d_k):
    two_norm = (np.dot(d_k.T, d_k).sum()) ** 0.5
    return two_norm


def calc_next_x(A, d_k, x_k):
    return x_k - np.dot(np.linalg.inv(A), d_k)


if __name__ == '__main__':
    dimension = 10

    A = create_A(dimension)
    print("A:\n", A, "\n")

    b = create_b(dimension)
    print("b:\n", b, "\n")

    x = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]).T
    print("x:\n", x, "\n")

    d = calc_first_order(A, b, x)
    print("2-norm of derivative:\n", calc_two_norm(d), "\n")

    iter_count = 1
    two_norm_list = [calc_two_norm(d)]
    while calc_two_norm(d) > 1e-15:
        print("-" * 50)

        x = calc_next_x(A, d, x)
        print("x:\n", x, "\n")

        d = calc_first_order(A, b, x)
        two_norm = calc_two_norm(d)
        two_norm_list.append(two_norm)
        print("2-norm of derivative:\n", two_norm, "\n")

        iter_count += 1

    plt.plot([x for x in range(iter_count)], two_norm_list)
    plt.show()
