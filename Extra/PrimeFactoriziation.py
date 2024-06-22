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
def count_divisions(n, d):
    if n%d==0:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        return count
Num=int(input())
for i in range(2,Num+1):
    if PrimeOrNot(i):
        x=i
        # print(i,count_divisions(Num,i))
        if count_divisions(Num,i):
            print(i,count_divisions(Num,i))
        # while Num%x==0:
        #     print(i,end=" ")
        #     x=x*i
# in this code we have first check if number is prime or not
# then we are checking if number is prime then how many times does it divides the given number
# we can check it by many ways one is above and other is here
# def count_divisions(n, d):
#     count = 0
#     while n % d == 0:
#         n //= d
#         count += 1
#     return count
# i have done some modification to get the desired results
