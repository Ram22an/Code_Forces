# this is my first approach by reading the question
# i thought that is is difficult question and i have used my brain a lot and thought that i have to find the min
# distance x1,x2,x3 have to travel for a point which is minimum like 
# if x1 and x2 and x3 have to reach that point they have to travel minimum distance 
# but the question is simple it only asked the distance from max-mid+mid-min like 
# what is the distance from x3 to x2 and x2 to x1 they have to reach the middle
# not the minimum distance they have to travel
# X1,X2,X3=map(int,input().split())
# MinVal=min(min(X1,X2),X3)
# MaxVal=max(max(X1,X2),X3)
# Arry=[X1,X2,X3]
# MidVal=0
# for i in Arry:
#     if i!=MinVal and i!=MaxVal:
#         MidVal=i
# if (X1+X2+X3)//3==MidVal:
#     print((MaxVal-MidVal)+(MidVal-MinVal))
# else:
#     Avg=(X1+X2+X3)//3
#     if Avg>MidVal:
#         print((MaxVal-Avg)+(Avg-MinVal)+(Avg-MidVal))
#     else:
#         print((MaxVal-Avg)+(Avg-MinVal)+(MidVal-Avg))




# final solution
X1,X2,X3=map(int,input().split())
Arry=[X1,X2,X3]
Arry.sort()
MinVal=Arry[0]
MidVal=Arry[1]
MaxVal=Arry[2]
print((Arry[2]-Arry[1])+(Arry[1]-Arry[0]))
