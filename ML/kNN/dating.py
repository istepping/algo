import numpy as np
import pandas as pd
import ML.kNN.knn as knn
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


# 读文件
def read_file(file):
    columns = ['里程数', '游戏占比', '公升数', '分类结果']
    # 文件名,列名,区分方式:1或多个空格
    df = pd.read_csv(file, names=columns, header=None, sep="\s+")
    group = df.ix[:, [0, 1, 2]].values  # 保留前三列
    label = df['分类结果'].values
    print(group)
    print(label)
    return group, label


# 数据的可视化
def data_visual(group, label):
    # 将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
    # 当nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex='none', sharey='none', figsize=(13, 8))
    label_count = len(label)
    # 颜色数组
    label_color = []
    for i in label:
        if i == 'didntLike':
            label_color.append('black')
        if i == 'smallDoses':
            label_color.append('orange')
        if i == 'largeDoses':
            label_color.append('red')
    # 第一个图，散点图,x轴:矩阵第一列，y轴:矩阵第二列,颜色,散点大小，透明度
    axs[0][0].scatter(x=group[:, 0], y=group[:, 1], color=label_color, s=15, alpha=0.5)
    axs0_title = axs[0][0].set_title(u"飞行与游戏占比")
    axs0_xlabel = axs[0][0].set_xlabel(u'飞行')
    axs0_ylabel = axs[0][0].set_ylabel(u'游戏')
    plt.setp(axs0_title, size=9, weight='bold', color='red')
    # 添加图例
    didntlike = mlines.Line2D([], [], color='black', marker='.', markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.', markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.', markersize=6, label='largeDoses')
    axs[0][0].legend(handles=[didntlike, smallDoses, largeDoses])
    # 第二个图，散点图,其他两个关系类似
    # 第三个图，散点图
    plt.show()


# 预测
def predict(test):
    groups, labels = read_file('datingTestSet.txt')
    return knn.classify_knn0(groups, labels, test, 10)


# 数据的归一化
def normalize(data_set):
    min_value = data_set.min(0)
    max_value = data_set.max(0)
    print(min_value)
    print(max_value)
    ranges = max_value - min_value
    norm_data_set = (data_set - np.tile(min_value, (data_set.shape[0], 1))) / np.tile(ranges, (data_set.shape[0], 1))
    print(norm_data_set)
    np.savetxt(r'normal_data.txt', norm_data_set)
    return norm_data_set


#############################
# @author sunLei
# @time 2018/12/8 20:06
# @note 训练数据和测试数据
#############################
def classify_tester(data_set, label, ratio=0.1):
    row_num = data_set.shape[0]  # 数据行数
    test_ratio = ratio  # 测试率
    test_num = int(row_num * test_ratio)  # 测试数据的个数
    error_count = 0.0  # 错误计数
    for i in range(test_num):
        classify_result = knn.classify_knn0(data_set[test_num:, :], label[test_num:], data_set[i, :], 4)
        if classify_result != label[i]:
            error_count += 1.0
    print("正确率:%f%%" % ((test_num - error_count) / float(test_num) * 100))


if __name__ == "__main__":
    file = 'datingTestSet.txt'
    group, label = read_file(file)
    # data_visual(group, label)
    nor_group = normalize(group)
    print("训练数据量增大正确率变化")
    classify_tester(nor_group, label,0.5)
    classify_tester(nor_group, label, 0.4)
    classify_tester(nor_group, label, 0.3)
    classify_tester(nor_group, label, 0.2)
    classify_tester(nor_group, label, 0.1)
    classify_tester(nor_group, label, 0.08)
    classify_tester(nor_group, label, 0.06)
    classify_tester(nor_group, label, 0.05)
    classify_tester(nor_group, label, 0.04)
    classify_tester(nor_group, label, 0.03)
    classify_tester(nor_group, label, 0.02)
    classify_tester(nor_group, label, 0.01)







