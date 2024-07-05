x=int(input())
for _ in range(x):
    Arr=list(map(int,input().split()))
    MinNum=min(Arr)
    MaxNum=max(Arr)
    Arr.remove(MinNum)
    Arr.remove(MaxNum)
    print(" ".join(map(str, Arr)))
