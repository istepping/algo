import numpy as np
import matplotlib.pyplot as plt

# init the matrix
A = np.zeros((10, 10))
b = np.ones((10, 1))
for i in range(10):
    for j in range(10):
        if i == j:
            A[i, j] = 2
        if abs(i - j) == 1:
            A[i, j] = A[j, i] = 1
x = np.zeros((10, 1))

# quasi_newton: DFP
B = np.identity(10)
d = A.dot(x) - b
d_2norm = np.dot(d.T, d).sum() ** 0.5
step = 0
norm_list = [d_2norm]
while d_2norm > 10 ** -1:
    x_next = x - 0.1* np.dot(np.linalg.inv(B), d)
    d = A.dot(x_next) - b
    d_2norm = np.dot(d.T, d).sum() ** 0.5
    y = (A.dot(x_next) - b) - (A.dot(x) - b)
    s = x_next - x
    B = B - (np.dot(B.dot(y), np.dot(y.T, B)) / np.dot(np.dot(y.T, B), y)) + (s.dot(s.T) / np.dot(y.T, s))
    x = x_next
    step += 1
    norm_list.append(d_2norm)

plt.plot([i for i in range(0, step + 1)], norm_list, "g-", label="quasi_newton")
plt.title("quasi_newton")
plt.xlabel("step")
plt.ylabel("2-norm")
plt.show()
