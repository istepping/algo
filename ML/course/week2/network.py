import random
import numpy as np
import matplotlib.pyplot as plt


class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)  # [784,15,10]每一层的神经元数
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]  # 除去输入层
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]  # (15,784),(10,15)

    def feedforward(self, a):
        # print("forward")
        count = 0
        for b, w in zip(self.biases, self.weights):
            if count == 1:
                # print("soft")
                a = softmax(np.dot(w, a) + b)
                # print(a)
            else:
                # print("relu")
                a = relu(np.dot(w, a) + b)
                # print(a)
            count += 1
        return a

    # mini-batch stochastic gradient descent
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        accuracy = []
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            print("epoch", j)
            random.shuffle(training_data)
            mini_batches = [training_data[k:k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)

            if test_data:
                predict = self.evaluate(test_data)
                print("Epoch {0}: {1} / {2}".format(
                    j, predict, n_test))
                accuracy.append(predict / n_test)
            else:
                print("Epoch {0} complete".format(j))
        plt.plot(range(epochs), accuracy, "-")
        plt.show()

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]  # 偏导数
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]  # 偏导数
        # print("更新")
        # print(self.weights)
        self.weights = [w - eta * nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - eta * nb for b, nb in zip(self.biases, nabla_b)]
        # print("更新后")
        # print(self.weights)

    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]  # list to store all the activations, layer by layer
        zs = []  # list to store all the z vectors, layer by layer
        count = 0
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            if count == 1:
                activation = softmax(z)
            else:
                activation = relu(z)
            count += 1
            activations.append(activation)
        # backward pass
        # 最后一层求导
        delta = self.cost_derivative(activations[-1], y)  # * relu_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # 前几层求导
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = relu_prime(z)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l - 1].transpose())
        return nabla_b, nabla_w

    def evaluate(self, test_data):
        x, y = test_data[0]
        # print(y)
        # print(self.weights)
        # print(self.biases)
        # print(self.feedforward(x))
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """Return the vector of partial derivatives \partial C_x /
        \partial a for the output activations."""
        return output_activations - y


def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))  # sigmoid的导数


def relu(z):
    return np.maximum(0, z)


def relu_prime(z):
    dz = np.array(z, copy=True)
    dz[dz > 0] = 1
    dz[dz <= 0] = 0
    return dz


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0, keepdims=True)
