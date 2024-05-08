NumberOfLevel=int(input())
arrX=[]
arrY=[]
arrX=list(map(int,input().split()))
arrY=list(map(int,input().split()))
arrYA=arrY[1:]
arrXA=arrX[1:]
final=[0]*NumberOfLevel
for i in range(1,NumberOfLevel+1):
    if i in arrXA:
        final[i-1]=1
    if i in arrYA:
        final[i-1]=1
if 0 in final:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")