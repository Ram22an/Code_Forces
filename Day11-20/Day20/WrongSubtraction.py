Number,Times=map(int,input().split())
for i in range(0,Times):
    Finding=Number%10
    if Finding>0:
        Number-=1
    else:
        Number=Number/10
print(int(Number))
