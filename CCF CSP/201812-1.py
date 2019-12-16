# 小明上学 #
# 读背景与描述
# 输入格式写输入
# 输出格式写输出
# 测试用例写算法
# 红灯秒 # 黄灯秒 # 绿灯秒
r,y,g=map(int,input().split())
num=int(input()) # 道路数或红绿灯数
time=0
for i in range(num):
    a=list(map(int,input().split()))
    if a[0]==0:
        time+=a[1]
    if a[0]==1:
        time+=a[1]
    if a[0]==2:
        time+=a[1]
        time+=r
print(time)

