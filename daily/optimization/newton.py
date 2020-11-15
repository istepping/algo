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
x = np.ones((10, 1))

# newton
d = A.dot(x) - b
d_2norm = np.dot(d.T, d).sum() ** 0.5
step = 0
norm_list = [d_2norm]
while d_2norm > 10 ** -5:
    x = x - np.dot(np.linalg.inv(A), d)
    d = A.dot(x) - b
    d_2norm = np.dot(d.T, d).sum() ** 0.5
    step += 1
    norm_list.append(d_2norm)

plt.plot([i for i in range(0, step + 1)], norm_list, "b-", label="newton")
plt.title("newton")
plt.xlabel("step")
plt.ylabel("2-norm")
plt.legend()
plt.show()
