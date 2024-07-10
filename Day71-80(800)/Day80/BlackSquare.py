Carolies=[0]
Carolies1=list(map(int,input().split(" ")))
Carolies+=Carolies1
StripStr=input()
Strips=list(map(int,StripStr))
Total=0
for i in range(len(Strips)):
    Total+=Carolies[Strips[i]]
print(Total)
# it is a easy question
