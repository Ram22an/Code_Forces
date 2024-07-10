NumberOFJuices=int(input())
arr=list(map(int,input().split(" ")))
Sum=0
for i in arr:
    Sum=Sum+i
print(Sum/NumberOFJuices)
