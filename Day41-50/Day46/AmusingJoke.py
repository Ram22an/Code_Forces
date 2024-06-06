FirstName=input()
SecondName=input()
MixedUp=input()
FirstName=FirstName.lower()
SecondName=SecondName.lower()
MixedUp=MixedUp.lower()
MixedUpList=[]
for i in MixedUp:
    MixedUpList.append(i)
if len(MixedUp)<len(FirstName)+len(SecondName) or len(MixedUp)>len(FirstName)+len(SecondName):
    print("NO")
else:
    FirstBool=True
    SecondBool=True
    # print(MixedUpList)
    for i in FirstName:
        if i in MixedUpList:
            MixedUpList.remove(i)
        else:
            FirstBool=False
    # print(MixedUpList)
    for i in SecondName:
        if i in MixedUpList:
            MixedUpList.remove(i)
        else:
            SecondBool=False
    # print(MixedUpList)
    if FirstBool and SecondBool:
        print("YES")
    else:
        print("NO")
        
