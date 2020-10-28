import numpy as np
import matplotlib.pyplot as plt

# 1. 矩阵初始化: 对角线元素全为2,当横纵坐标系数差的绝对值为1时，矩阵元素值是1
A = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        if i == j:
            A[i, j] = 2
        if abs(i - j) == 1:
            A[i, j] = A[j, i] = 1
b = np.ones((100, 1))
x = np.zeros((100, 1))  # 给定初始值

# 2. 共轭梯度法
r = b - A.dot(x)  # 矩阵运算r0
p = r  # p0=r0
step = 0
Y = []
# 共轭梯度法在n步迭代内能够的到精确解
for i in range(100):
    a = np.dot(r.T, p) / np.dot(p.T, A.dot(p))
    x = x + a * p
    Y.append(np.linalg.norm(A.dot(x) - b))
    if np.linalg.norm(A.dot(x) - b) < 10 ** -6:
        step = i + 1
        break
    else:
        r = b - A.dot(x)
        beta = np.dot(r.T, A.dot(p)) / np.dot(p.T, A.dot(p))
        p = r - beta * p

# 3. 可视化与分析: 迭代次数和函数值结果下降
print([i for i in range(1, step + 1)])
print(Y)
plt.plot([i for i in range(1, step + 1)], Y, "b-", label="CG")
plt.title("Conjugate Gradient Method")
plt.xlabel("step")
plt.ylabel("value")
plt.show()

