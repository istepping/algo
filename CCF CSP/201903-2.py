# 输入
n=int(input())
a=[]
for i in range(n):
    a.append(input())
for s in a:
    s=s.replace("/","//")
    s=s.replace("x","*")
    result=eval(s) # 计算表达式
    if result==24:
        print("Yes")
    else:
        print("No")
