Times=int(input())
for i in range(Times):
    x=int(input())
    arry=[]
    while x>0:
        arry.append(x%10)
        x=x//10
    Final=[]
    counter=0
    for i in range(len(arry)):
        Ans=arry[i]*10**i
        if Ans>0:
            counter+=1
            Final.append(Ans)
    print(counter)
    Final_str = [str(item) for item in Final]
    print(" ".join(Final_str))
# it is good question it required good thinking 
