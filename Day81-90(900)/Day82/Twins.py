NumOfCoins=int(input())
Arry=list(map(int,input().split()))
Arry.sort()
TotalSum=0
for i in Arry:
    TotalSum+=i
counter=0
MoneyWanted=0
while True:
    temp=Arry.pop()
    counter+=1
    MoneyWanted+=temp
    TotalSum-=temp
    if counter<=NumOfCoins and MoneyWanted>TotalSum:
        break
print(counter)
