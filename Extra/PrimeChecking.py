# it is naive method it have time complexity is O(n)
Num=int(input())
if Num==1:
    print("False")
else:
    counter=0
    for i in range(2,Num):
        if Num%i==0:
            print("False")
            counter=0
            break
        else:
            counter=1
    if counter==1:
        print("True")
# here is the another approach 
# x=int(input())
# if Num==1:
#     print("False")
# else:
n = int(input("Enter the value of n: "))
for i in range(2, int(n**0.5) + 1):
    # print(i, i*i)
    if n%i==0:
        print("No")
        break

x=2
while x*x<=n:
    if n%i==0:
        print("NO")
        break
    x+=1
# here is the more optimized approach 
counter=0
if n==1:
    print("NO")
    counter=1
if n==2 or n==3:
    print("YES")
    counter=0
if n%2==0 or n%3==0:
    print("NO")
    counter=1
for i in range(5,int(n**0.5)+1,6):
    if n%1==0 or n%(i+2)==0:
        print("NO")
        counter=1
if counter==0:
    print("YES")
    