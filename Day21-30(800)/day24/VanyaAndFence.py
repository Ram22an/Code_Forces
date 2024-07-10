NumberOfFriend,HeightOfFence=map(int,input().split())
Arr=[]
WidthOfRoad=0
Arr=list(map(int,input().split()))
for i in range(NumberOfFriend):
    if Arr[i]>HeightOfFence:
        WidthOfRoad+=2
    else:
        WidthOfRoad+=1
print(WidthOfRoad)
# it was easy as compare to the Tram question