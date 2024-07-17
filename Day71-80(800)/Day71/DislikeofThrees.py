# x=1666
# i=1
# arr=[]
# while i<x+1:
#     if i%3==0 or i%10==3:
#         continue
#     else:
#         arr.append(i)
#     i+=1
# print(arr)
# this what i have sbumited but i don't liked this method 
# x1 = 1666
# i = 0
# arr = []
# while  i<=x1:
#     if i % 3 != 0 and i % 10 != 3:
#         arr.append(i)
#     i += 1
# # print(arr)
# print(len(arr))
# x=int(input())
# for _ in range(x):
#     a=int(input())
#     print(arr[a-1])
# here is the another method
# x=int(input())
# for _ in range(x):
#     Num=int(input())
#     i=1
#     while Num!=0:
#         if i%3==0 or i%10==0:
#             i+=1
#         else:
#             Num-=1
#             if Num==0:
#                 print(i)
#             i+=1
x = int(input())  # number of test cases
for _ in range(x):
    Num = int(input())  # read each test case input
    count = 0  # to count the valid numbers
    for i in range(1, Num + 1):
        while i % 3 == 0 or i % 10 == 3:
            i += 1
        count += 1  # increment count for valid number found
        if count == Num:
            print(i)
            break
x = int(input())  # Number of test cases
for _ in range(x):
    Num = int(input())  # Input number for each test case
    count = 0  # Counter to track the valid numbers
    for i in range(1, 10000):  # Loop over numbers from 1 to a large number (adjust as needed)
        if i % 3 == 0 or i % 10 == 3:
            continue  # Skip this number if it's divisible by 3 or ends with 3
        else:
            count += 1  # Increment count for valid numbers
        if count == Num:  # If we've found the Num-th valid number
            print(i)  # Print the number and break out of the loop
            break
# here are the variation this code that i found online and able to understand and easy to use 
