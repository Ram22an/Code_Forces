NumberOfFriend=int(input())
arr=list(map(int,input().split()))
# 4
# 2 3 4 1
# here 1 ko gift diya 2 ne or 2 ko gift diya 3 ne or 3 ko gift diya 4 ne or 4 ko gift diya 1 ne
# and output will be 1 ne diya 4 ko gift
arr1=[None]+[0]*(NumberOfFriend)
for i in range(NumberOfFriend):
    arr1[arr[i]]=i+1
ans=list(arr1[1:])
print(" ".join(map(str,ans)))
