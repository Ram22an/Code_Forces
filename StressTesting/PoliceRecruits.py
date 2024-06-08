import random
# x=int(input())
# Crime=list(map(int,input().split()))
# CrimeOccured=0
# PoliceAva=0
# for i in Crime:
#     if i!=-1:
#         PoliceAva+=i
#     else:
#         if PoliceAva>0:
#             PoliceAva-=1
#         else:
#             CrimeOccured+=1
# print(CrimeOccured)


# this was my approach for first time

x=random.randint(1, 100000)
print(x)
Crime=[]
for i in range(x):
    a=random.randint(-1,10)
    if a==0:
        a=1
    Crime.append(a)
counter=0
print(Crime)
# finding last -1
for i in range(x):
    if Crime[i]==-1:
        counter=i
Crime2=Crime[:counter+1]
Final=0
for i in Crime2:
    if i==-1:
        Final+=1
    else:
        Final-=i
if Final<0:
    Final=0
print(Final)