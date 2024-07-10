num=int(input())
arr=[]
for i in range(num):
    a,b=map(int,input().split())
    ans=0
    if a%b==0:
        ans=0
    else:
        ans=a%b
        ans=b-ans
    arr.append(ans)
print( *[i for i in arr],sep="\n")

# here we have learned a new thing that is when we do a%b
# let ans=a%b
# so number of steps is equal to b-ans
