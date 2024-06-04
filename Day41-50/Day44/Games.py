x=int(input())
home=[]
guest=[]
for i in range(x):
    x1,x2=map(int,input().split())
    home.append(x1)
    guest.append(x2)
counter=0
for i in range(x):
    for j in range(x):
        if home[i]==guest[j]:
            counter+=1
print(counter)