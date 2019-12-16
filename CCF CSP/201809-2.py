# 买菜:求相交时间段
# 输入
n=int(input())# 时间段数量
# H的时间段
H=[]
for i in range(n):
    a=list(map(int,input().split()))
    H.append(a)
# W的时间段
W=[]
for i in range(n):
    a=list(map(int,input().split()))
    W.append(a)
chat=0 # 聊天时长
# 两边相互弹出迭代至有一边为空
while(len(H)!=0 and len(W)!=0):
    a=H[0]
    b=W[0]
    # 抉择出最大左边界
    if(a[0]<b[0]):
        left=b[0]
    else:
        left=a[0]
    # 抉择出最小右边界
    if(a[1]<b[1]):
        right=a[1]
        # 最小的部分弹出
        H.pop(0)
    else:
        right=b[1]
        # 最小的部分弹出
        W.pop(0)
    # 存在交叉区间
    if(right>left):
        chat+=right-left
# 程序输出
print(chat)
