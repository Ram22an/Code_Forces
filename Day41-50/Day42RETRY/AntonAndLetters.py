StringList=list(map(str,input().strip().split(",")))
if len(StringList)>2:
    StringList[0]=StringList[0][1:]
    StringList[-1]=StringList[-1][:-1]
    StringList2=[element.strip() for element in StringList]
    Dir1=set(StringList2)
    print(len(Dir1))
else:
    # trying again
    print(0)
    # this is for streak
    