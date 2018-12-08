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
# @time 2018/12/8 21:21
# @note 特征值系数训练
#############################
def weight_train(group, label):
    k = 5  # k值
    weight = [0.1, 0.1, 0.1, 0.1]  # 系数数组
    step = 0.1  # 步长
    ranges = 10  # 训练范围
    right_count = 0.0  # 正确的数量
    max_right = 0.0  # 最大的正确率
    max_right_weight = [0.1, 0.1, 0.1]  # 最大正确率时的系数
    finish_num = 0.0  # 已经完成数
    total_num = ranges ** 4  # 总数
    test_num = 9  # 测试数据数
    train_data = group[test_num:, :]
    train_label = label[test_num:]
    for A in range(ranges):
        weight[0] = weight[0] + A * step
        for B in range(ranges):
            weight[1] = weight[1] + B * step
            for C in range(ranges):
                weight[2] = weight[2] + C * step
                for D in range(ranges):
                    weight[3] = weight[3] + D * step
                    print(weight)
                    for i in range(test_num):
                        classify_result = knn.classify_knn0(train_data, train_label, group[i, :], k)
                        if classify_result == label[i]:
                            right_count += 1.0
                    ratio = right_count / float(test_num)
                    if ratio > max_right:
                        max_right = ratio
                        max_right_weight = weight
                    weight[3] = 0.1  # 归位
                    finish_num += 0.1  # 进度加一
                weight[2] = 0.1  # 归位
            weight[1] = 0.1  # 归位
        weight[0] = 0.1  # 归位
        print("进度:%f" % (finish_num / total_num))
    print("最大率", max_right)
    print("结果", max_right_weight)


if __name__ == "__main__":
    group1, label1 = read_file(r'data_bill.txt')
    nor_group = knn.normalize(group1)
    weight_train(nor_group, label1)
