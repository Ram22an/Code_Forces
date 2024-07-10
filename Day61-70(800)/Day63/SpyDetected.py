x=int(input())
for i in range(x):
    Size=int(input())
    Arry=list(map(int,input().split()))
    for i in Arry:
        Count=Arry.count(i)
        if Count==1:
            Value=i
            break
    print(Arry.index(Value)+1)
# here is the brute force method without count 
FirstCount=1
FirstIndex=0
FirstVal=Arry[0]
SecondCount=0
SecondIndex=0
SecondVal=0
for i in range(1,Size):
    if Arry[i]==FirstVal:
        FirstCount+=1
        FirstIndex=i
    else:
        SecondCount+=1
        SecondIndex=i
        SecondVal=Arry[i]
if SecondCount>1:
    Value=FirstIndex+1
else:
    Value=SecondIndex+1
print(Value)
