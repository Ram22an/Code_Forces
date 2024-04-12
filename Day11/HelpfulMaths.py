Question=input()
Arr=[]
for i in Question:
    if i!="+":
        Arr.append(i)
    else:
        pass
Arr.sort()
print("+".join(Arr))
# this is simple logic for sort 
# for i in range(0,len(try1)):
#     for j in range(i,len(try1)):
#         if try1[i] > try1[j]:
#             temp=try1[i]
#             try1[i]=try1[j]
#             try1[j]=temp
# print(try1)