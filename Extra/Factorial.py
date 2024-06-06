def Recursive(x):
    if x<=1:
        return 1
    else:
        return x*Recursive(x-1)
x=int(input())
a=Recursive(x)
# print(a)
# anotherCounter=0
# while a!=0:
#     if a%10==0:
#         anotherCounter+=1
#     else:
#         break
#     a=a//10
# print(anotherCounter)
# if x>1:
#     Sum=1
#     while x>0:
#         Sum=Sum*x
#         x-=1
#     print(Sum)
# else:
#     print(1)
