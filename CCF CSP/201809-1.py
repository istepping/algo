# 卖菜
# 1-n,ceil()向上取整 floor()向下取整 round()四舍五入,保留小数位数
# 输入
import math
import random

n = int(input())  # 卖菜个数
price = list(map(int, input().split()))  # 菜价
price2 = []  # 第二天菜价
for i in range(n):
    if i == 0:
        price2.append(math.floor((price[i] + price[i + 1]) / 2))
    elif i == n - 1:
        price2.append(math.floor((price[i - 1] + price[i]) / 2))
    else:
        price2.append(math.floor((price[i - 1] + price[i] + price[i + 1]) / 3))
for i in range(n):
    print(price2[i], end=" ")
