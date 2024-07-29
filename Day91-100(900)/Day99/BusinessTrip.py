def Merge(arr,left,mid,right):
    Arry=[]
    Low=left
    Center=mid+1
    while Low<=mid and Center<=right:
        if arr[Low]<=arr[Center]:
            Arry.append(arr[Low])
            Low+=1
        else:
            Arry.append(arr[Center])
            Center+=1
    while Low<=mid:
        Arry.append(arr[Low])
        Low+=1
    while Center<=right:
        Arry.append(arr[Center])
        Center+=1
    for i in range(left,right+1):
        arr[i]=Arry[i-left]
def MergerSort(arr,left,right):
    if left>=right:
        return
    mid=(left+right)//2
    MergerSort(arr,left,mid)
    MergerSort(arr,mid+1,right)
    Merge(arr,left,mid,right)
Centimeter=int(input())
countCenti=Centimeter
Months=list(map(int,input().split()))
MergerSort(Months,0,11)
Months = Months[::-1]
counter = 0
Add = 0
while Centimeter > 0 and counter < 12:
    Centimeter -= Months[counter]
    Add += Months[counter]
    counter += 1
# counter=0
# Add=0
# while Centimeter>0:
#     Centimeter-=Months[-1]
#     Add+=Months.pop()
#     counter+=1
if Add<countCenti:
    print(-1)
else:
    print(counter)
# there was a mistake or you can say there is lack of condition in while loop
# there is not such necessary to go for reversed order of the array
# it was simple question
