NumCont=int(input())
ArryPoint=list(map(int,input().split()))
Best=ArryPoint[0]
Worst=ArryPoint[0]
counter=0
for i in ArryPoint:
    if i<Worst:
        counter+=1
        Worst=i
    if i>Best:
        counter+=1
        Best=i
print(counter)