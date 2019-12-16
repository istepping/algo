# 跳一跳
jump=list(map(int,input().split()))
score=0 # 记录分数
last_score=0 # 记录上一次得分
for i in jump:
    if i==1:
        score+=1
        last_score=1
    if i==2:
        if last_score<=1:
            score+=2
            last_score=2
        else:
            score=score+last_score+2
            last_score+=2
print(score)
