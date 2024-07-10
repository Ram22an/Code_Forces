x=int(input())
for _ in range(x):
    Timur,FirstPer,SecondPer,ThirdPer=map(int,input().split())
    counter=0
    if Timur<FirstPer:
        counter+=1
    if Timur<SecondPer:
        counter+=1
    if Timur<ThirdPer:
        counter+=1
    print(counter)
