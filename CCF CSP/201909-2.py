# 输入格式
N=int(input()) # 棵树
total=[] # 最后苹果数
start_num=[] # 开始苹果数
throw_num=[] #蔬果数
for i in range(N):
    d=list(map(int,input().split()))
    num=d[0] # 后面数字个数
    start_num.append(d[1])
    a=d[1:] # 后续参数
    # 逆序遍历
    for i,data in enumerate(reversed(a)):
        if data>0:
            total.append(sum(a[len(a)-1-i:]))
            break
    sum_num=0 # 累计疏果数
    for data in a:
        if data <=0:
            sum_num+=data
    throw_num.append(sum_num)
D=0 #计算D
has_down=[0]*N #记录是否有掉落
for i,data in enumerate(start_num):
    if data+throw_num[i]!=total[i]:
        D+=1 # 有掉落
        has_down[i]=1

E=0 # 计算E
for i,data in enumerate(has_down):
    if data==1 and has_down[(i-1)%N]==1 and has_down[(i+1)%N]==1:
        E+=1
# 进行统计操作
print(sum(total),D,E)
