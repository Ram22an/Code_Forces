def Recursive(x):
    if x<=1:
        return 1
    else:
        return x*Recursive(x-1)
x=int(input())
print(Recursive(x))
# if x>1:
#     Sum=1
#     while x>0:
#         Sum=Sum*x
#         x-=1
#     print(Sum)
# else:
#     print(1)
