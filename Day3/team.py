size=int(input())
wins=0
for i in range(0,size):
    friend1=int(input())
    friend2=int(input())
    friend3=int(input())
    if friend1+friend2+friend3>=2:
        wins+=1
print(wins)
