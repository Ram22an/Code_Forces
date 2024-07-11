Var=input()
Arry=list(map(int,Var))
For1=0
For0=0
TrueOrFalse=True
for i in Arry:
    if i==1:
        For0=0
        For1+=1
        if For1==7:
            print("YES")
            TrueOrFalse=False
            break
    if i==0:
        For1=0
        For0+=1
        if For0==7:
            print("YES")
            TrueOrFalse=False
            break
if TrueOrFalse:
    print("NO")
