NumberOfPeople,Time=map(int,input().split())
arr=list(input())
for i in range(Time):
    for j in range(NumberOfPeople-1):
        if arr[j]=='B' and arr[j+1]=='G':
            # print(arr[j],arr[j+1],j)
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            j=j+1
print("".join(arr))