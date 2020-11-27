import torch
from torch import nn, optim
import matplotlib.pyplot as plt
from BPNet import BPNet
import numpy as np

batch_size = 10
learning_rate = 0.9
weight_decay = 0.01
epochs = 300
output = 3
# 加载数据
data = torch.from_numpy(np.loadtxt(r"data.txt", delimiter="  ", dtype=np.float32))
X = data[:, 0:3]
Y = data[:, 3:]
print(X)
print(Y)
# 训练模型
model = BPNet(3, 5, 4)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=weight_decay)
model.train()
loss_value = []
mini_loss = 100
for i in range(epochs):
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, Y)
    loss_value.append(loss)
    loss.backward()
    optimizer.step()
    if loss < mini_loss:
        torch.save(model.state_dict(), "model.pth")
    mini_loss = loss

model.load_state_dict(torch.load("model.pth"))

Y = model(X)
print(Y)
# 预测结果
plt.plot(range(epochs), loss_value, '-')
plt.show()
