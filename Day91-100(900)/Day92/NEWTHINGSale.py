def Merge(TvArray,high,mid,low):
    arr=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if TvArray[left]<=TvArray[right]:
            arr.append(TvArray[left])
            left+=1
        else:
            arr.append(TvArray[right])
            right+=1
    while left<=mid:
        arr.append(TvArray[left])
        left+=1
    while right<=high:
        arr.append(TvArray[right])
        right+=1
    for i in range(low,high+1):
        TvArray[i]=arr[i-low]
def MergerSort(TvArray,high,low):
    if low>=high:
        return
    mid=(low+high)//2
    MergerSort(TvArray,mid,low)
    MergerSort(TvArray,high,mid+1)
    Merge(TvArray,high,mid,low)
Size,Needed=map(int,input().split())
TVArray=list(map(int,input().split()))
High=Size-1
Low=0
Price=0
MergerSort(TVArray,High,Low)
for i in range(0,Needed):
    if TVArray[i]<=0:
        Price+=TVArray[i]*-1
print(Price)
# it was easy question but i have learned new sorting algo
# that is merge sort
