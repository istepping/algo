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
x = np.zeros((10, 1))
# SD
q = np.linalg.norm(A.dot(x) - b) / np.linalg.norm(b)
step2 = 0
Y = []
while np.linalg.norm(A.dot(x) - b) > 10 ** -5:
    r = A.dot(x) - b
    a = np.dot(r.T, r) / np.dot(r.T, A.dot(r))
    x = x - a * r
    step2 += 1
    Y.append(np.linalg.norm(A.dot(x) - b))

# visual
plt.plot([i for i in range(1, step2 + 1)], Y, "r-", label="SD")
plt.title("SD")
plt.xlabel("step")
plt.ylabel("2-norm")
plt.legend()
plt.show()
