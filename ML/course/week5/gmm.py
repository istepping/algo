import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

X_train = np.array([1, 1.3, 2.2, 2.6, 2.8, 5, 7.3, 7.4, 7.5, 7.7, 7.9])
X_train = X_train.reshape(-1, 1)
model = GaussianMixture(n_components=2, means_init=np.array([6, 7.5]).reshape(2, 1), covariance_type='tied')
model.fit(X_train)
prediction = model.predict(X_train)

print(prediction)
class1 = []
class2 = []
for index, it in enumerate(prediction):
    if it == 0:
        class1.append(X_train[index])
    else:
        class2.append(X_train[index])
plt.plot(class1,np.zeros_like(class1), "^", label="cluster1")
plt.plot(class2,np.zeros_like(class2), "+", label="cluster2")
plt.legend()
plt.show()
