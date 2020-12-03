import numpy as np
import pandas as pd
from scipy.io import loadmat
from sklearn import svm
import matplotlib.pyplot as plt

train_mat = loadmat(r'D:\doc\2020\MachineLearning\第三次作业\垃圾邮件训练和测试数据\spamTrain.mat')
test_mat = loadmat(r'D:\doc\2020\MachineLearning\第三次作业\垃圾邮件训练和测试数据\spamTest.mat')
train_df = pd.DataFrame(train_mat.get('X'))
train_df['Y'] = train_mat.get('y')
print(train_df.head())
# 使用Pegasos算法训练(loss设置为hinge),C设为0.1
c = 1 # 从[0.01,1]间隔0.01和[1,100]间隔0.01分别测试
c_list = []
score_list = []
while c <= 100:
    model = svm.LinearSVC(C=c, loss='hinge', max_iter=1000)
    X_train = train_mat['X']
    Y_train = train_mat['y'].ravel()  # 变成一维数组
    X_test = test_mat['Xtest']
    Y_test = test_mat['ytest'].ravel()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    c_list.append(c)
    score_list.append(score)
    c +=1
plt.plot(c_list, score_list, '-')
plt.show()
print(max(score_list),c_list[score_list.index(max(score_list))])
