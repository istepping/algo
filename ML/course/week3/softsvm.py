import numpy as np
import pandas as pd
from scipy.io import loadmat
from sklearn import svm
train_mat = loadmat(r'D:\doc\2020\MachineLearning\第三次作业\垃圾邮件训练和测试数据\spamTrain.mat')
test_mat = loadmat(r'D:\doc\2020\MachineLearning\第三次作业\垃圾邮件训练和测试数据\spamTest.mat')
train_df = pd.DataFrame(train_mat.get('X'))
train_df['Y'] = train_mat.get('y')
print(train_df.head())
# 使用Pegasos算法训练(loss设置为hinge),C设为0.1
model = svm.LinearSVC(C=0.1, loss='hinge', max_iter=1000)
X_train = train_mat['X']
Y_train = train_mat['y'].ravel()  # 变成一维数组
X_test = test_mat['Xtest']
Y_test = test_mat['ytest'].ravel()
model.fit(X_train, Y_train)
score = model.score(X_test, Y_test)
print(score)
