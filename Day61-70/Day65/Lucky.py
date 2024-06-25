x=int(input())
for _ in range(x):
    Num=int(input())
    LastNum=Num%1000
    FirstNum=Num//1000
    LastSum=0
    FirstSum=0
    for i in range(3):
        temp=LastNum%10
        LastNum=LastNum//10
        LastSum+=temp
        temp2=FirstNum%10
        FirstNum=FirstNum//10
        FirstSum+=temp2
    if LastSum==FirstSum:
        print("YES")
    else:
        print("NO")
