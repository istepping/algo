import numpy as np
import matplotlib.pyplot as plt

# comparison with SD
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
# CG
r = b - A.dot(x)
p = r  # p0=r0
step = 0
Y = []
for i in range(10):
    a = np.dot(r.T, p) / np.dot(p.T, A.dot(p))
    x = x + a * p
    Y.append(np.linalg.norm(A.dot(x) - b))
    q = np.linalg.norm(A.dot(x) - b) / np.linalg.norm(b)
    if q < 10 ** -6:
        step = i + 1
        break
    else:
        r = b - A.dot(x)
        beta = np.dot(r.T, A.dot(p)) / np.dot(p.T, A.dot(p))
        p = r - beta * p
# SD
x = np.zeros((10, 1))
q = np.linalg.norm(A.dot(x) - b) / np.linalg.norm(b)
step2 = 0
Y2 = []
while np.linalg.norm(A.dot(x) - b) > 10 ** -6:
    r = b - A.dot(x)
    print(np.dot(r.T, A.dot(r)))
    a = np.dot(r.T, r) / np.dot(r.T, A.dot(r))
    x = x + a * r
    step2 += 1
    Y2.append(np.linalg.norm(A.dot(x) - b))

# visual
plt.plot([i for i in range(1, step + 1)], Y, "b-", label="CG")
plt.plot([i for i in range(1, step2 + 1)], Y2, "r-", label="SD")
plt.title("CG and SD")
plt.xlabel("step")
plt.ylabel("value")
plt.legend()
plt.show()
