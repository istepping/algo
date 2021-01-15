import numpy as np
from sklearn.decomposition import PCA
import os
from PIL import Image
import matplotlib.pyplot as plt

X = []
file_dict = r'D:\doc\2020\MachineLearning\第六次作业\orl_faces'
for item in os.listdir(file_dict):
    for item2 in os.listdir(file_dict + "\\" + item):
        image = Image.open(file_dict + "\\" + item + "\\" + item2)
        x = np.asarray(image)  # 112*92
        x = x.flatten()
        X.append(x)

X = np.array(X)  # 400*10304, 400张图片,10304个特征

fig, objs = plt.subplots(3, 5, subplot_kw={"xticks": [], "yticks": []})
# objs:3*5的数组
for i, obj in enumerate(objs.flat):
    obj.imshow(X[i].reshape(112, 92), cmap='gray')
fig.show()
pca = PCA(n_components=100) # n_components="mle"使用概率PCA极大似然估计算法或EM算法求解
pca = pca.fit(X)
result=pca.components_
fig2,objs2=plt.subplots(3,5,subplot_kw={"xticks": [], "yticks": []})
for i, obj2 in enumerate(objs2.flat):
    obj2.imshow(result[i].reshape(112,92), cmap='gray')
fig2.show()

