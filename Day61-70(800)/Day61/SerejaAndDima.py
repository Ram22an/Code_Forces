Size=int(input())
Arry=list(map(int,input().split()))
Sereja=0
Dima=0
for i in range(Size):
    if i%2==0:
        if Arry[0]>Arry[-1]:
            Sereja+=Arry.pop(0)
        else:
            Sereja+=Arry.pop(-1)
    else:
        if Arry[0]>Arry[-1]:
            Dima+=Arry.pop(0)
        else:
            Dima+=Arry.pop(-1)
print(f"{Sereja} {Dima}")
# this is also correct but we can make it more optimize with 
# making it small in size like 
sereja = 0
dima = 0

for i in range(Size):
    if Arry[0] > Arry[-1]:
        choice = Arry.pop(0)
    else:
        choice = Arry.pop(-1)
    
    if i % 2 == 0:
        sereja += choice
    else:
        dima += choice
# in this we have reduced the code with removing the hardcoded lines 
