def Merger(Arr,Left,Mid,Right):
    low=Left
    Center=Mid+1
    Temp=[]
    while low<=Mid and Center<=Right:
        if Arr[low]<Arr[Center]:
            Temp.append(Arr[low])
            low+=1
        else:
            Temp.append(Arr[Center])
            Center+=1
    while low<=Mid:
        Temp.append(Arr[low])
        low+=1
    while Center<=Right:
        Temp.append(Arr[Center])
        Center+=1
    for i in range(Left,Right+1):
        Arr[i]=Temp[i-Left]
def MergerSort(Arr,Left,Right):
    if Left>=Right:
        return
    Mid=(Left+Right)//2
    MergerSort(Arr,Left,Mid)
    MergerSort(Arr,Mid+1,Right)
    Merger(Arr,Left,Mid,Right)


x=int(input())
for _ in range(x):
    Size,Diff=map(int,input().split())
    Questions=list(map(int,input().split()))
    MergerSort(Questions,0,Size-1)
    # correct logic uses sliding window
    max_len = 1
    current_len = 1
    # here we are iterating through the array
    for i in range(1, Size):
        # checking if the the consecutive item does have the difference smaller than diff or not
        if Questions[i] - Questions[i - 1] <= Diff:
            current_len += 1
        else:
            # if not we are changing the max len to the max of max len or current len
            max_len = max(max_len, current_len)
            current_len = 1
    # checking the last iterating
    max_len = max(max_len, current_len)
    print(Size-max_len)
    
    # this was my pervious logic and it was not correct
    # Temp=[]
    # for i in range(Size-1):
    #     if Questions[i+1]-Questions[i]>Diff:
    #         Temp=Questions[i+1:]
    # if len(Temp)!=0:
    #     print(len(Questions)-len(Temp))
    # else:
    #     print(0)
