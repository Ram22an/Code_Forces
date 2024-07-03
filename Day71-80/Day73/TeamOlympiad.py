Size=int(input())
Arr2=list(map(int,input().split()))
# it is my approach 
# countof1=Arr2.count(1)
# countof2=Arr2.count(2)
# countof3=Arr2.count(3)
# Ans=min(countof1,countof2,countof3)
# print(Ans)
# print(Arr)
# for idx, num in enumerate(Arr2):
#     if num
# print(Ans)
# if Ans>0:
#     for _ in range(Ans):
#         print(Arr2.index(1),Arr2.index(2),Arr2.index(3),end="\n")
#         Arr2[Arr2.index(1)]=0
#         Arr2[Arr2.index(2)]=0
#         Arr2[Arr2.index(3)]=0
# print(Ans)
# print(Arr)
# here is the another approach from online
Maths=[]
Programing=[]
PhysicalEduaction=[]
countof1=Arr2.count(1)
countof2=Arr2.count(2)
countof3=Arr2.count(3)
Ans=min(countof1,countof2,countof3)
print(Ans)
for index,i in enumerate(Arr2):
    if i==1:
        Programing.append(index+1)
    if i==2:
        Maths.append(index+1)
    if i==3:
        PhysicalEduaction.append(index+1)
# print(Ans)
# print(min(len(Programing),len(Maths),len(PhysicalEduaction)))
for i in range(Ans):
    print(Programing[i],Maths[i],PhysicalEduaction[i])
