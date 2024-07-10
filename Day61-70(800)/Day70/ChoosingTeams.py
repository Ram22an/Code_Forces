NumStudent,NumOfParti=map(int,input().split())
Arry=list(map(int,input().split()))
SecondArry=[]
for i in range(NumStudent):
    if Arry[i]+NumOfParti<=5:
        SecondArry.append(Arry[i])
print(len(SecondArry)//3)
