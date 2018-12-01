from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt  # 可视化库类似matlab
price=datasets.load_boston()
price_x=price.data
price_y=price.target
print(price_x)
print(price_y)
model=LinearRegression()
model.fit(price_x,price_y)
print(model.predict(price_x[:4,:]))
print(price_y[:4])
x,y=datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=10)
plt.scatter(x,y)
plt.show()
