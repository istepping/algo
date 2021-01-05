import pandas as pd
import numpy as np

from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

df = pd.read_csv("data.csv")
data = np.array(df)
X_train, y_train = data[:, 0:2], data[:, -1]
model1 = QuadraticDiscriminantAnalysis()
model2 = GaussianNB()

pred1 = model1.fit(X_train, y_train).predict(np.array([[0.5, 0.3]]))
pred2 = model2.fit(X_train, y_train).predict(np.array([[0.5, 0.3]]))
print("The Prediction Result of Quadratic Discriminant Analysis is: {}".format(pred1))
print("The Prediction Result of Gaussian Naive Bayes is: {}".format(pred2))
