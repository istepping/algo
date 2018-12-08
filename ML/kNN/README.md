# 电影分类实例
* 最近邻近算法
通过距离向量计算最近的点
1. k-邻近算法的步骤
* 计算输入数据与已知数据的距离向量
* 按照递增次序排序
* 选取前k个值
* 将前k个值中类别频率最大的类别作为输出结果
# 海伦约会
1. 数据特征
* 每年获得的飞行常客里程数
* 玩视频游戏所消耗的时间百分比
* 每周消费的冰淇凌公升数
2. 数据的归一化
* 不同特征值的权重
* 映射方式:newValue=(oldValue-min)/(max-min)
# 相关
1. sorted()
* sort,list成员函数
* sorted可以对所有可迭代对象进行排序
2. read_csv()
3. DataFrame
* 类似excel数据结构
创建
``
df=pd.DataFrame(np.random(4,4),index=list('ABCD'),columns=list('ABCD'))
``
* 转换二维数组
pd.values()
4. 数组写入到文件中
``
numpy方式
np.savetxt(r'normal_data.txt',norm_data_set)
列表方式
file=open('data.txt','w')
file.write(str(list_data))
file.close()
``













# 参考
[](https://cuijiahua.com/blog/2017/11/ml_1_knn.html)