size=int(input())
realX=0
for i in range(0,size):
    word=input()
    if word[0]=="X" or word[-1]=="X":
        if word[1]=="-":
            realX-=1
        else:
            realX+=1
print(realX)
