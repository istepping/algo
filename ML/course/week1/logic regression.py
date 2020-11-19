import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(linewidth=200, precision=5, suppress=True)


# Sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


data = np.loadtxt(r"D:\doc\2020\机器学习\第一周\ex2data2.txt", delimiter=',')  # size=(118,3)

X = np.array(data)[:, 0:2]  # X=(118,2)
Y = np.array(data)[:, 2].reshape((-1, 1))  # Y=(118,1)
print(X.shape[0])
X = np.insert(X, 0, values=np.ones(X.shape[0]), axis=1)
X = np.insert(X, 3, X[:, 1] ** 2, axis=1)
X = np.insert(X, 4, X[:, 2] ** 2, axis=1)
X = np.insert(X, 5, X[:, 1] * X[:, 2], axis=1)
print(X)
# 模型, Z=W0X0+W1X1+W2X2+W3X1^2+W4X2^2+W5X1X2  等同于进行特征空间的映射[x1,x2]=>[x1,x2,x1^2,x2^2,x1x2]
W = np.ones((6, 1))  # 模型参数初始值
lr = 0.1  # 学习率
iteration = 1000  # 迭代次数
for i in range(iteration):
    W = W + lr * np.dot(X.T, (Y - sigmoid(np.dot(X, W))))  # 梯度上升算法
# 计算预测准确率
TP, FP, FN, TN = 0, 0, 0, 0
pred = sigmoid(X.dot(W))
for i in range(pred.shape[0]):
    if pred[i][0] >= 0.5:
        if Y[i][0] == 1:
            TP += 1
        else:
            FP += 1
    else:
        if Y[i][0] == 1:
            FN += 1
        else:
            TN += 1
P, R = TP / (TP + FP), TP / (TP + FN)  # 计算准确率和查全率
F1 = 2 * P * R / (P + R)  # 计算F1 score
print("P=", P)
print("R=", R)
print("F1=", F1)
# 可视化结果
X1, X2 = np.meshgrid(np.arange(-1, 1.3, 0.1), np.arange(-1, 1.3, 0.1))
Z = W[0] + W[1] * X1 + W[2] * X2 + W[3] * (X1 ** 2) + W[4] * (X2 ** 2) + W[5] * X1 * X2
plt.figure()
class1 = []
class2 = []
for item in data:
    if item[2] == 1:
        class1.append(item)
    else:
        class2.append(item)
plt.plot(np.array(class1)[:, 0], np.array(class1)[:, 1], "^", label="class1")
plt.plot(np.array(class2)[:, 0], np.array(class2)[:, 1], "s", label="class2")
plt.contour(X1, X2, Z, levels=0)
plt.legend()
plt.show()
