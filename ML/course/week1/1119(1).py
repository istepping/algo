
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt


data = np.loadtxt('ex2data2.txt', delimiter=',')
print(data[:2],'\n', data.shape)

X = data[:, 0:2]
y = data[:, 2]

# print(X[:, 0])

def plot_data(X, y):
    plt.figure()
    
    X0 = X[y==0]
    X1 = X[y==1]
    plt.scatter(X0[:, 0], X0[:, 1], c='g', marker='^')
    plt.scatter(X1[:, 0], X1[:, 1], c='b', marker='o')
    
plot_data(X, y)

plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.legend(['y = 1', 'y = 0'])

def map_feature(x1, x2):
    degree = 6
    # print('x1shape:',x1.shape,x1)
    x1 = x1.reshape((x1.size, 1))#一列
    # print('after x1shape:',x1.shape,x1)
    x2 = x2.reshape((x2.size, 1))
    result = np.ones(x1[:, 0].shape)
    # print('result_shape:',result.shape,result)
    
    for i in range(1, degree + 1):
        for j in range(0, i + 1):
            result = np.c_[result, (x1**(i-j)) * (x2**j)]#按行连接两个矩阵
    return result#(118, 28)

X = map_feature(X[:, 0], X[:, 1])
print(X.shape)

def sigmoid(z):
    g = 1 / (1 + np.exp(-z))
    return g

def cost_function_reg(theta, X, y, lmd):
    m = y.size

    cost = 0
    grad = np.zeros(theta.shape)

	#逻辑回归假设函数
    hypothesis = sigmoid(np.dot(X, theta))
    #由于正则化不包含theta0，剔除theta0参数
    reg_theta = theta[1:]
    # 含正则化的代价函数
    cost = np.sum(-y * np.log(hypothesis) - (1 - y) * np.log(1 - hypothesis)) / m + (lmd / (2 * m)) * np.sum(reg_theta * reg_theta)
    # 梯度下降，不含正则化
    normal_grad = (np.dot(X.T, hypothesis - y) / m).flatten()

    grad[0] = normal_grad[0]
    #对批量题库下降除theta0外部分参数进行正则化处理
    grad[1:] = normal_grad[1:] + reg_theta * (lmd / m)

    return cost, grad

# Initialize fitting parameters 28个0
initial_theta = np.zeros(X.shape[1])

# Set regularization parameter lambda to 1
lmd = 1

# Compute and display initial cost and gradient for regularized logistic regression
cost, grad = cost_function_reg(initial_theta, X, y, lmd)

np.set_printoptions(formatter={'float': '{: 0.4f}\n'.format})
print('Cost at initial theta (zeros): {}'.format(cost))
print('Expected cost (approx): 0.693')
print('Gradient at initial theta (zeros) - first five values only: \n{}'.format(grad[0:5]))
print('Expected gradients (approx) - first five values only: \n 0.0085\n 0.0188\n 0.0001\n 0.0503\n 0.0115')

# Compute and display cost and gradient with non-zero theta
test_theta = np.ones(X.shape[1])

cost, grad = cost_function_reg(test_theta, X, y, lmd)

print('Cost at test theta: {}'.format(cost))
print('Expected cost (approx): 2.13')
print('Gradient at test theta - first five values only: \n{}'.format(grad[0:5]))
print('Expected gradients (approx) - first five values only: \n 0.3460\n 0.0851\n 0.1185\n 0.1506\n 0.0159')

# Initializa fitting parameters
initial_theta = np.zeros(X.shape[1])

# Set regularization parameter lambda to 1 (you should vary this)
lmd = 1

# Optimize
def cost_func(t):
    return cost_function_reg(t, X, y, lmd)[0]
def grad_func(t):
    return cost_function_reg(t, X, y, lmd)[1]

theta, cost, *unused = opt.fmin_bfgs(f=cost_func, fprime=grad_func, x0=initial_theta, maxiter=400, full_output=True, disp=False)

def plot_decision_boundary(theta, X, y):
    plot_data(X[:, 1:3], y)

    if X.shape[1] <= 3:
        # 取第一门考试成绩最大最小值坐标
        plot_x = np.array([np.min(X[:, 1]) - 2, np.max(X[:, 1]) + 2])
        # 计算决策边界线算法通过第一门考试成绩最大最小值和theta计算决策边界线的第二门考试成绩两点坐标，以便绘制决策边界线
        # 即通过两点绘制一条直线(决策边界线)
        plot_y = (-1/theta[2]) * (theta[1]*plot_x + theta[0])
        plt.plot(plot_x, plot_y)
        plt.legend(['Decision Boundary', 'Admitted', 'Not admitted'], loc=1)
        plt.axis([30, 100, 30, 100])
    else:
        # Here is the grid range
        u = np.linspace(-1, 1.5, 50)
        v = np.linspace(-1, 1.5, 50)

        z = np.zeros((u.size, v.size))

        # Evaluate z = theta*x over the grid
        for i in range(0, u.size):
            for j in range(0, v.size):
                z[i, j] = np.dot(map_feature(u[i], v[j]), theta)

        z = z.T

        # Plot z = 0
        # Notice you need to specify the range [0, 0]
        cs = plt.contour(u, v, z, levels=[0], colors='r')
        plt.legend([cs.collections[0]], ['Decision Boundary'])
        
# Plot boundary
print('Plotting decision boundary ...')
plot_decision_boundary(theta, X, y)
plt.title('lambda = {}'.format(lmd))

plt.xlabel('Microchip Test 1')
plt.ylabel('Microchip Test 2')
plt.show()




















