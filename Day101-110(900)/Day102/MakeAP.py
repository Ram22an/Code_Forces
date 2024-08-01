# i have also provided a image to understand ap
# it is like a+bm=bm+c or am+b=b+c or a+b=b+cm
x=int(input())
for _ in range(x):
    a,b,c=map(int,input().split())
    if (2*b-c)%a==0 and (2*b-c)/a>0:
        print("YES")
    elif (c+a)%(2*b)==0 and (c+a)/(2*b)>0:
        print("YES")
    elif (2*b-a)%c==0 and (2*b-a)/c>0:
        print("YES")
    else:
        print("NO")
# this code is copied and today i don't have fresh mind to do the question
# sorry for this
