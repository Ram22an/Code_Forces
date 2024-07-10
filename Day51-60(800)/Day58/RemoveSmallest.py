x=int(input())
for i in range(x):
    Size=int(input())
    arry=list(map(int,input().split()))
    arry.sort()
    FinalAns="YES"
    if Size>1:
        for i in range(Size-1):
            if abs(arry[i]-arry[i+1])>1:
                FinalAns="NO"
                break
    print(FinalAns)
