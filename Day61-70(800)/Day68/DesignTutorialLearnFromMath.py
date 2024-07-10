def PrimeOrNot(Num):
    if Num==1:
        return False
    if Num ==2 or Num==3:
        return True
    if Num%2==0 or Num%3==0:
        return False
    for i in range(5,int(Num**0.5)+1,6):
        if Num%i==0 or Num%(i+2)==0:
            return False
    return True
Num=int(input())
for i in range(4,Num+1):
    x=i
    y=Num-x
    if not PrimeOrNot(x) and not PrimeOrNot(y):
        print(x,y)
        break
