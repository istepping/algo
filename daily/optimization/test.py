import numpy as np
import matplotlib.pyplot as plt

# init
A = np.zeros((10, 10))
b = np.ones((10, 1))
for i in range(10):
    for j in range(10):
        if i == j:
            A[i, j] = 2
        if abs(i - j) == 1:
            A[i, j] = A[j, i] = 1
x = np.ones((10, 1))

# SD
step = 0
d = A.dot(x) - b
Y = [np.dot(d.T, d).sum() ** 0.5]
while np.dot(d.T, d).sum() ** 0.5 > 10 ** -3:
    r = b - A.dot(x)
    a = np.dot(r.T, r) / np.dot(r.T, A.dot(r))
    x = x + a * r
    step += 1
    Y.append(np.linalg.norm(A.dot(x) - b))
    d = A.dot(x) - b
print("SD Method\n", x)

# newton
x = np.ones((10, 1))
d_first_order = A.dot(x) - b
d_2norm = np.dot(d_first_order.T, d_first_order).sum() ** 0.5
step2 = 0
norm_list = [d_2norm]
while d_2norm > 10 ** -3:
    x = x - np.dot(np.linalg.inv(A), d_first_order)
    d_first_order = A.dot(x) - b
    d_2norm = np.dot(d_first_order.T, d_first_order).sum() ** 0.5
    step2 += 1
    norm_list.append(d_2norm)
print("Newton's Method\n", x)

# quasi_newton: DFP
x = np.ones((10, 1))
B = np.identity(10)
d = A.dot(x) - b
d_2norm = np.dot(d.T, d).sum() ** 0.5
step3 = 0
norm_list2 = [d_2norm]
while d_2norm > 10 ** -1:
    x_next = x - 0.1 * np.dot(np.linalg.inv(B), d)
    d = A.dot(x_next) - b
    d_2norm = np.dot(d.T, d).sum() ** 0.5
    y = (A.dot(x_next) - b) - (A.dot(x) - b)
    s = x_next - x
    B = B - (np.dot(B.dot(y), np.dot(y.T, B)) / np.dot(np.dot(y.T, B), y)) + (s.dot(s.T) / np.dot(y.T, s))
    x = x_next
    step3 += 1
    norm_list2.append(d_2norm)
print("Quasi Newton Method\n", x)

# visual
plt.plot([i for i in range(0, step + 1)], Y, "r-", label="SD")
plt.plot([i for i in range(0, step2 + 1)], norm_list, "b-", label="Newton")
plt.plot([i for i in range(0, step3 + 1)], norm_list2, "g-", label="QuasiNewton")
plt.title("comparison of the error tendency")
plt.xlabel("step")
plt.ylabel("2-norm")
plt.legend()
plt.show()
