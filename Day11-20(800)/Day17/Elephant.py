Position=int(input())
Steps=0
while Position>=5:
    Position-=5
    Steps+=1
while Position>=4:
    Position-=4
    Steps+=1
while Position>=3:
    Position-=3
    Steps+=1
while Position>=2:
    Position-=2
    Steps+=1
while Position>=1:
    Position-=1
    Steps+=1
print(Steps)