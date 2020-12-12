import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from sklearn import linear_model


def dict_update(y, d, x, n_components):
    for i in range(n_components):
        index = np.nonzero(x[i, :])[0]
        if len(index) == 0:
            continue
        # 更新第i列
        d[:, i] = 0
        # 计算误差矩阵
        r = (y - np.dot(d, x))[:, index]
        # 利用svd的方法，来求解更新字典和稀疏系数矩阵
        u, s, v = np.linalg.svd(r, full_matrices=False)
        # 使用左奇异矩阵的第0列更新字典
        d[:, i] = u[:, 0]
        # 使用第0个奇异值和右奇异矩阵的第0行的乘积更新稀疏系数矩阵
        for j, k in enumerate(index):
            x[i, k] = s[0] * v[0, j]
    return d, x


X = []
file_dict = r'D:\doc\2020\MachineLearning\第四次作业\orl_faces'
for item in os.listdir(file_dict):
    for item2 in os.listdir(file_dict + "\\" + item):
        image = Image.open(file_dict + "\\" + item + "\\" + item2)
        x = np.asarray(image)
        x = x.flatten()
        X.append(x)
        print(image)
        break
X=np.array(X).T
print(X.shape) # (10304,400)
u, s, v = np.linalg.svd(X)
k = 50  # 设置字典词汇量
dict_data = u[:, :k]

max_iter = 20
tol = 1e-6  # 误差范围
e_list = []
for i in range(max_iter):
    X_ = linear_model.orthogonal_mp(dict_data, X)
    e = np.linalg.norm(X - np.dot(dict_data, X_))
    e_list.append(e)
    if e < tol:
        break
    dict_update(X, dict_data, X_, k)

sparsecode = linear_model.orthogonal_mp(dict_data, X)
print(sparsecode.shape) # (50,400)
train_restruct = dict_data.dot(sparsecode)
plt.plot(range(len(e_list)), e_list, '-')
plt.show()
