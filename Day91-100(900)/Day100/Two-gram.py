Size=int(input())
String=input()
Element={}
for i in range(Size-1):
    temp=String[i:i+2]
    if temp in Element:
        Element[temp]+=1
    else:
        Element[temp]=1
print(max(Element,key=Element.get))
# this question was looking very difficult but it was easy
# this question is good implementation of dictionary
