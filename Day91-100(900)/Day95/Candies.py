# def PrimeOrNot(num):
#     if num==1:
#         return False
#     if num==2 or num==3:
#         return True
#     if num%2==0 or num%3==0:
#         return False
#     for i in range(5,int(num**0.5)+1,6):
#         if num%(i+1)==0 or num%i==0:
#             return False
#     return True
x=int(input())
for _ in range(x):
    num=int(input())
    # there is no need for checking prime number 
    # if PrimeOrNot(num):
    #     print(1)
    # else:
        # here is the formula for geometric progression is (r**k-1)
        # for this question 2^k-1 and it is equal to x*(2^k-1)=n
        # so we have to check for all the value starting from 2 to n
    k = 2
    while True:
        sum_series = (2 ** k) - 1  # This is 2^k - 1
        if num % sum_series == 0:
            print( num // sum_series)
            break
        k += 1
