# 再卖菜-最优化算法-拿20分
import math
n=int(input())
price=list(map(int,input().split()))
flag=True
find=False
# 验证序列是否可行的函数
def search(price0,i,root):
    global find
    if len(price0)==i+1:
        if root<1 or math.ceil((root+price0[i-1])/2)!=price[i]:
            pass
        else:
            find=True
    else:
        if root<1:
            pass # 结束递归不符合要求
        else:
            search(price0,i+1,price0[i+1]) # 左子树
            search(price,i+1,price0[i+1]+1) # 右子树

price0=[0]*n
price0[0]=1
while flag:
    for j in range(n-1):
        i=j+1
        if i==1:
            price0[i]=price[i-1]*2-price0[i-1]
        else:
            price0[i]=price[i-1]*3-price[i-1]-price[i-2]
    # 构建二叉树:left=price0[i] 右子树；right=price0[i]+1 深度优先搜索
    print(price0)
    search(price0,0,price0[0])
    if find:
        flag=False
    else:
        price0[0]+=1
# 输出
for i in range(n):
    print(price0[i],end=" ")
