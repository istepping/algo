# 输入
n=int(input())
a=list(map(int,input().split()))
# 数据处理
if n%2==0:
    mid=(a[(n-1)//2]+a[n//2])/2
else:
    mid=a[n//2]
if int(mid)==mid:
    mid=int(mid)
# 输出
print(max(a),mid,min(a))
