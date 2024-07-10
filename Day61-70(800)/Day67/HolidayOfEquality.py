Size=int(input())
Arry=list(map(int,input().split()))
MaxNum=max(Arry)
MoneyNeed=0
for i in Arry:
    if i<=MaxNum:
        MoneyNeed+=(MaxNum-i)
print(MoneyNeed)
