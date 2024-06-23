x=int(input())
for i in range(x):
    Size=int(input())
    Arry=list(map(int,input().split()))
    for i in Arry:
        Count=Arry.count(i)
        if Count==1:
            Value=i
            break
    print(Arry.index(Value)+1)
