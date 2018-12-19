import numpy as np
import operator


def classify_knn1(data_set, label, test_data, k):
    data_set_size = data_set.shape[0]  # 行数
    # numpy.tile(),np.tile(a,(2,1))# 把a 在x轴复制1倍，y轴复制2倍
    minus_mat = np.tile(test_data, (data_set_size, 1)) - data_set
    # sum()全部相加,sum(0),列相加，sum(1),行相加
    distances = ((minus_mat ** 2).sum(axis=1)) ** 0.5
    sorted_distances = distances.argsort()  # 从小到大排序后返回索引值
    class_count = {}  # 统计次数的字典
    for i in range(k):
        vote_label = label[sorted_distances[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1  # 次数加一
    class_ratio = []  # 分类比率
    print(class_count)
    for i in range(6):
        class_ratio.append(round(class_count.get(i + 1, 0) / k, 2))
    return class_ratio


# dataSet:训练集,label标签，testData:测试数据,k:K值
def classify_knn0(data_set, label, test_data, k):
    data_set_size = data_set.shape[0]  # 行数
    # numpy.tile(),np.tile(a,(2,1))# 把a 在x轴复制1倍，y轴复制2倍
    minus_mat = np.tile(test_data, (data_set_size, 1)) - data_set
    # sum()全部相加,sum(0),列相加，sum(1),行相加
    distances = ((minus_mat ** 2).sum(axis=1)) ** 0.5
    sorted_distances = distances.argsort()  # 从小到大排序后返回索引值
    class_count = {}  # 统计次数的字典
    for i in range(k):
        vote_label = label[sorted_distances[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


# 数据的归一化
def normalize(data_set):
    min_value = data_set.min(0)
    max_value = data_set.max(0)
    ranges = max_value - min_value
    norm_data_set = (data_set - np.tile(min_value, (data_set.shape[0], 1))) / np.tile(ranges, (data_set.shape[0], 1))
    # np.savetxt(r'normal_data.txt', norm_data_set)
    return norm_data_set, min_value, max_value
