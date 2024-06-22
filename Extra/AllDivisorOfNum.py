# here we are finding divisor of a number 
# we could simply find it by running the loop from 1 to n
# and finding all the number 
# but here is the optimize approach here we are doing x*y=Num
# then we can use it y=Num//x and go for half the value of Num
# we will get all the divisor in pair  
Num=int(input())
Arry=[]
for i in range(1,int(Num**0.5)+1):
    if Num%i==0:
        x=Num//i
        if x not in Arry:
            Arry.append(x)
        if i not in Arry:
            Arry.append(i)
Arry.sort()
print(" ".join(map(str,Arry)))
