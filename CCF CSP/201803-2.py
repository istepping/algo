n,L,t=map(int,input().split())
loc=list(map(int,input().split()))
speed=[1]*n # 1表示向右,-1表示向左
for i in range(t):
    for j in range(n):
        # 跟新位置
        loc[j]=loc[j]+speed[j]*1 
    for j in range(n):    
        # 改变速度方向
        if loc[j]==0 or loc[j]==L or loc.count(loc[j])>1:
            speed[j]=-speed[j]
        
print(" ".join(str(i) for i in loc))            
    
    
