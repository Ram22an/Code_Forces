x=int(input())
for i in range(x):
    a,b,c=map(int,input().split())
    if a+b==c:
        print("YES")
    elif a+c==b:
        print("YES")
    elif c+b==a:
        print("YES")
    else:
        print("NO")
