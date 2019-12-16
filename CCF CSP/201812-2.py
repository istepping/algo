# 小明放学
r,y,g=map(int,input().split())
circle=r+y+g
n=int(input())
time=0 # 累计时间
for i in range(n):
    a=list(map(int,input().split()))
    current=time%circle
    flag=a[0]
    left=a[1]
    if a[1]>current:
        left=a[1]-current
    else:
        temp=current-a[1]
        if a[0]==1:
            if temp<y:
                flag=2
                left=y-temp
            elif temp<y+g:
                flag=3
                left=g-(temp-y)
            else:
                flag=1
                left=r-(temp-y-g)
        if a[0]==2:
            print("原来是是%d,temp是%d"%(2,temp))
            if temp<g:
                print("现在是%d"%3)
                flag=3
                left=g-temp
            elif temp<g+r:
                print("现在是%d"%1)
                flag=1
                left=r-(temp-g)
            else:
                print("现在是%d"%2)
                flag=2
                left=y-(temp-g-r)
        if a[0]==3:
            if temp<r:
                flag=1
                left=r-temp
            elif temp<r+y:
                flag=2
                left=y-(temp-r)
            else:
                flag=3
                left=g-(temp-r-y)
    print(flag,left)
    # 路口没灯
    if a[0]==0:
        time+=a[1]
        print(a[1])
    if flag==1:
        time+=left
        print(left)
    if flag==2:
        time+=left
        time+=r
        print(left+r)
print(time)
