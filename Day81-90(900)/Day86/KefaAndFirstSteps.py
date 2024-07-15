Size=int(input())
Arry=list(map(int,input().split()))
# Ans,i,j=0,0,0
# while i<Size-1:
#     if Arry[i]<=Arry[i+1]:
#         j=i
#         temp=0
#         while j<Size-1 and Arry[j] <= Arry[j + 1]:
#             temp+=1
#             j+=1
#         Ans=max(temp+1,Ans)
#         i=j
#     else:
#         i+=1
# print(Ans)
# this is my code and it is exceeding time limite on test case 8
# it might need some tweak 

temp,Ans=1,1
for i in range(Size-1):
    if Arry[i]<=Arry[i+1]:
        temp+=1
        if temp>Ans:
            Ans=temp
    else:
        temp=1
print(Ans)
# i don't know why my pervious code is exceeding time in which i tried to 
# decrease the loops with help of conditions but this code with out conition 
# traversing through all the array is not exceeding the time 
