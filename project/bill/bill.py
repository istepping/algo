import numpy as np
import pandas as pd
import ML.kNN.knn as knn
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


# 读文件
def read_file(file):
    columns = ['A', 'B', 'C', 'D', 'E']
    df = pd.read_csv(file, names=columns, header=None, sep="\s+")
    return df.ix[:, [0, 1, 2, 3]].values, df['E'].values


#############################
# @author sunLei
# @time 2018/12/8 23:39
# @note 预测器
#############################
def predict(test):
    group, label = read_file(r'data_bill.txt')
    normal_group = knn.normalize(group)
    return knn.classify_knn0(group, label, test, 5)


#############################
# @author sunLei
# @time 2018/12/8 21:21
# @note 特征值系数训练
#############################
def weight_train(group, label, step=0.1, ranges=10, k=3, test_num=10):
    print(group)
    k = k  # k值
    weight = [0.1, 0.1, 0.1, 0.1]  # 系数数组
    step = step  # 步长
    ranges = ranges  # 训练范围
    right_count = 0.0  # 正确的数量
    max_right = 0.0  # 最大的正确率
    max_right_weight = [0.1, 0.1, 0.1, 0.1]  # 最大正确率时的系数
    finish_num = 0.0  # 已经完成数
    total_num = ranges ** 4  # 总数
    test_num = test_num  # 测试数据数
    train_data = group[test_num:, :]
    train_label = label[test_num:]
    for A in range(ranges):
        weight[0] = round(0.1 + A * step, 1)
        for B in range(ranges):
            weight[1] = round(0.1 + B * step, 1)
            for C in range(ranges):
                weight[2] = round(0.1 + C * step, 1)
                for D in range(ranges):
                    weight[3] = round(0.1 + D * step, 1)
                    for i in range(test_num):
                        classify_result = knn.classify_knn0(train_data, train_label, group[i, :], k)
                        if classify_result == label[i]:
                            right_count += 1.0
                    ratio = right_count / float(test_num)

                    if ratio > max_right:
                        print("替换")
                        max_right = ratio
                        max_right_weight[:] = weight[:]  # 赋值
                        print(max_right_weight)
                    finish_num += 1.0  # 进度加一
                    right_count = 0.0  # 归位
        print("进度:%f" % (finish_num / total_num))
    print("正确率", max_right)
    print("结果", max_right_weight)


if __name__ == "__main__":
    print(predict([0.5, 0.34, 0.12, 60]))
    # group1, label1 = read_file(r'data_bill.txt')
    # nor_group = knn.normalize(group1)
    # weight_train(nor_group, label1, step=1, ranges=10, k=3, test_num=5)
