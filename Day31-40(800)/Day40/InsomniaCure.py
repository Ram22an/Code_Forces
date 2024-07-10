FryingPan=int(input())
BalconyDoor=int(input())
SharpHeels=int(input())
HerMom=int(input())
TotalDragon=int(input())
counter=0
for i in range(1,TotalDragon+1):
    if i%FryingPan==0 or i%BalconyDoor==0 or i%SharpHeels==0 or i%HerMom==0:
        counter+=1
print(counter)
