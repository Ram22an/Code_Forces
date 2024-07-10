NumberOfRooms=int(input())
NumberOfAvailable=0
for i in range(NumberOfRooms):
    People,Capacity=map(int,input().split())
    if Capacity-People>=2:
        NumberOfAvailable+=1
print(NumberOfAvailable)