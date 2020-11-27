import network2
import mnist_loader
import matplotlib.pyplot as plt

# 加载数据并分为训练数据、验证数据和测试数据
train_data, validation_data, test_data = mnist_loader.load_data_wrapper()
# 使用神经网络模型
model = network2.Network([28 * 28, 15, 10])
# 设置训练参数,eta是学习率
model.SGD(train_data, epochs=30, mini_batch_size=10, eta=8.0,evaluation_data=test_data,monitor_evaluation_accuracy=True)
# 结果可视化

# plt.plot(range(0, 30), [0.8959,0.9082,0.9123,0.9175,0.9237,0.9193,0.9194,0.9254,0.9275,0.9273,0.9280,0.9293,0.9296,0.9317,0.9292,0.9315,0.9290,0.9305,0.9322,0.9259,0.9298,0.9316,0.9312,0.9339,0.9334,0.9300,0.9340,0.9350,0.9350,0.9350], "-")
# plt.xlabel("epoch")
# plt.ylabel("accuracy")
# plt.show()
