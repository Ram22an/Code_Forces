# import random
# X1=random.randint(1, 100)
# X2=random.randint(1, 100)
# X3=random.randint(1, 100)
X1,X2,X3=map(int,input().split())
# print(X1,X2,X3)

Arry=[X1,X2,X3]
Arry.sort()
MinVal=Arry[0]
MidVal=Arry[1]
MaxVal=Arry[2]
# print(MinVal,MidVal,MaxVal)
# MinDis=(MinVal+MaxVal)//2+((MinVal+MaxVal)//2-MidVal)
# print((MaxVal-MinDis)+(MidVal-MinDis)+(MinDis-MinVal))
# print((MaxVal-MinDis))
# print((MidVal-MinDis))
# print((MinDis-MinVal))
print((Arry[2]-Arry[1])+(Arry[1]-Arry[0]))