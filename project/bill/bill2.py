import numpy as np
import pandas as pd
import ML.kNN.knn as knn
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import datetime


# 读文件
def read_file(file):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'R']
    df = pd.read_csv(file, names=columns, header=None, sep="\s+")
    return df.ix[:, [0, 1, 2, 3, 4, 5]].values, df['R'].values


#############################
# @author sunLei
# @time 2018/12/8 23:39
# @note 预测器
#############################
def predict(test):
    group, label = read_file(r'data_bill.txt')
    # 加载系数
    test = test * np.loadtxt("max_right_weight.txt")
    return knn.classify_knn0(group, label, test, 20)


def save_weight(weight):
    with open(r"max_right_weight.txt", 'w') as f:
        f.write("%.2f" % weight[0])
        f.write("\t")
        f.write("%.2f" % weight[1])
        f.write("\t")
        f.write("%.2f" % weight[2])
        f.write("\t")
        f.write("%.2f" % weight[3])
        f.write("\t")
        f.write("%.2f" % weight[4])
        f.write("\t")
        f.write("%.2f" % weight[5])


#############################
# @author sunLei
# @time 2018/12/8 21:21
# @note 特征值系数训练
#############################
def weight_train(group, label, step=0.1, ranges=10, k=3, test_num=0.3):
    k = k  # k值
    weight = [1, 1, 1, 1, 1, 1]  # 系数数组
    step = step  # 步长
    ranges = ranges  # 训练范围
    right_count = 0.0  # 正确的数量
    max_right = 0.0  # 最大的正确率
    max_right_weight = [0.1, 0.1, 0.1, 0.1]  # 最大正确率时的系数
    finish_num = 0.0  # 已经完成数
    total_num = ranges ** 6  # 总数
    test_num = int(test_num * group.shape[0])  # 测试数据数
    train_data = group[test_num:, :]
    train_label = label[test_num:]
    time = datetime.datetime.now()
    print("进度:%f" % (finish_num / total_num))
    print(test_num)
    during = 0.0
    for A in range(ranges):
        weight[0] = round(0.1 + A * step, 1)
        for B in range(ranges):
            weight[1] = round(0.1 + B * step, 1)
            for C in range(ranges):
                weight[2] = round(0.1 + C * step, 1)
                for D in range(ranges):
                    weight[3] = round(0.1 + D * step, 1)
                    for E in range(ranges):
                        weight[4] = round(0.1 + E * step, 1)
                        for F in range(ranges):
                            weight[5] = round(0.1 + F * step, 1)
                            for i in range(test_num):
                                test_data = group[i, :] * weight
                                classify_result = knn.classify_knn0(train_data, train_label, test_data, k)
                                if classify_result == label[i]:
                                    right_count += 1.0
                            ratio = right_count / float(test_num)
                            if ratio == 1.0:
                                # 训练完成,提前结束
                                print("得到最佳结果，提前结束")
                                print("正确率", ratio)
                                print("结果", weight[:])
                                save_weight(weight[:])
                            if ratio > max_right:
                                max_right = ratio
                                max_right_weight[:] = weight[:]  # 赋值
                                print("替换")
                                print(ratio, max_right_weight)
                            finish_num += 1.0  # 进度加一
                            right_count = 0.0  # 归位
                    print("进度:%f" % (finish_num / total_num))
                    # 时间处理
                    if D == 0:
                        now = datetime.datetime.now()
                        during = (now - time).seconds
                        during = during / finish_num
                        print("平均时间", during)

                    next_during = int(during * (total_num - finish_num))  # 还需要得时间戳
                    print(next_during)
                    time_month = trans_time(next_during // (60 * 60 * 24 * 30))
                    time_day = trans_time(next_during // (60 * 60 * 24) % 30)
                    time_hours = trans_time(next_during // (60 * 60) % 24)
                    time_minute = trans_time(next_during // 60 % 60)
                    print("剩余时间:{0}月{1}天{2}小时{3}分钟".format(time_month, time_day, time_hours, time_minute))
    print("正确率", max_right)
    print("结果", max_right_weight)
    save_weight(max_right_weight)


def trans_time(t):
    if t > 9:
        return t
    else:
        return '0' + str(t)


if __name__ == "__main__":
    group1, label1 = read_file(r'data_bill.txt')
    weight_train(group1, label1, step=1, ranges=4, k=20, test_num=0.001)
    # print(predict(np.array([0.9, 0.34, 0.22, 0.2, 0.2, 0.2])))
