# this is giving run time error becuse it is slow in python we can do this in cpp it is working 
size, position = map(int, input().split())
arr=[]
nextRound=0
for i in range(size):
    x=int(input())
    arr.append(x)
for i in range(size):
    if arr[i]>=arr[position-1] and arr[i]>0:
        nextRound+=1
print(nextRound)
