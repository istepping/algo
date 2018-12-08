# 准备数据
# kNN算法
# 测试
import numpy as np
import operator


def create_data_set():
    group = np.array([[1, 101], [5, 89], [108, 5], [115, 8]])
    label = ['爱情片', '爱情片', '动作片', '动作片']
    return group, label


# dataSet:训练集,label标签，testData:测试数据,k:K值
def classify_knn0(dataSet, label, testData, k):
    data_set_size = dataSet.shape[0]  # 行数
    # numpy.tile(),np.tile(a,(2,1))# 把a 在x轴复制1倍，y轴复制2倍
    minus_mat = np.tile(testData, (data_set_size, 1)) - dataSet
    # sum()全部相加,sum(0),列相加，sum(1),行相加
    distances = ((minus_mat ** 2).sum(axis=1)) ** 0.5
    sorted_distances = distances.argsort()  # 从小到大排序后返回索引值
    class_count = {}  # 统计次数的字典
    for i in range(k):
        vote_label = label[sorted_distances[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


if __name__ == '__main__':
    group, label = create_data_set()
    test = [100, 150]
    print(classify_knn0(group, label, test, 3))
