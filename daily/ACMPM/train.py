import torch
from torch import nn, optim
import matplotlib.pyplot as plt
from BPNet import BPNet
import numpy as np

batch_size = 10
learning_rate = 0.9
weight_decay = 0.01
epochs = 100
output = 3
# 加载数据
data = torch.from_numpy(np.load(r"data.txt", delimiter=','))
X = torch.randn(batch_size, 3)
Y = torch.randn(batch_size, 3)
# 训练模型
model = BPNet(3, 5, 3)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
model.train()
loss_value = []
for i in range(epochs):
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, Y)
    loss_value.append(loss)
    loss.backward()
    optimizer.step()

# 预测结果
plt.plot(range(epochs), loss_value, '-')
plt.show()
