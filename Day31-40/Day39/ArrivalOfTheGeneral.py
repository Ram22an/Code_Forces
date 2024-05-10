# i don't know why my code is failing i have tried with my logic and also with yt logic

NumberOfSoldier=int(input())
ArrayOfSoldiers=list(map(int,input().split()))
arr=[]
MaxElement=0
MaxIndex=0
MinElement=100
MinIndex=0
for i in range(0,NumberOfSoldier):
    if ArrayOfSoldiers[i]>=MaxElement:
        MaxElement=ArrayOfSoldiers[i]
        MaxIndex=i
    if ArrayOfSoldiers[i]<=MinElement:
        MinElement=ArrayOfSoldiers[i]
        MinIndex=i
# print(MaxElement,MaxIndex)
# print(MinElement,MinIndex)
# while MaxIndex>0:
#     MaxIndex-=1
#     TotalWork+=1
# while(MinIndex<NumberOfSoldier-1):
#     MinIndex+=1
#     TotalWork+=1
if MaxIndex>=MinIndex:
    print((MaxIndex-1)+(NumberOfSoldier-MinIndex)-1)
else:
    print((MaxIndex-1)+(NumberOfSoldier-MinIndex))
# while True:
#     if MinIndex==NumberOfSoldier-1 and MaxIndex==0:
#         break
#     if MinIndex<NumberOfSoldier-1 :
#         temp=ArrayOfSoldiers[MinIndex]
#         ArrayOfSoldiers[MinIndex]=ArrayOfSoldiers[MinIndex+1]
#         ArrayOfSoldiers[MinIndex+1]=temp
#         MinIndex+=1
#         TotalWork+=1
#     if MaxIndex>0:
#         temp=ArrayOfSoldiers[MaxIndex]
#         ArrayOfSoldiers[MaxIndex]=ArrayOfSoldiers[MaxIndex-1]
#         ArrayOfSoldiers[MaxIndex-1]=temp
#         MaxIndex-=1
#         TotalWork+=1
