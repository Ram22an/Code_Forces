x=int(input())
if x>=0:
    print(x)
else:
    x=x*-1
    temp2=x%100
    temp=temp2%10
    temp3=temp2//10
    if temp>temp3:
        x=x//10
        print(x*-1)
    else:
        x=x//100
        x=x*10+temp
        print(x*-1)
# it was a easy question
