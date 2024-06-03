import re
Line=input()
if len(Line)>2:
    ListOfWords=re.split(r'[{ },]',Line)
    # here is the code implementation of re 
    # Trying=[]
    # for i in Line:
    #     if i==" " or i=='{' or i=='}' or i==',':
    #         Trying.append("")
    #     else:
    #         Trying.append(i)
    # print(Trying)
    # Trying2=[]
    # for i in Trying:
    #     if i!="":
    #         Trying2.append(i)
    # print(Trying2)

    ListOfWords2 = [word for word in ListOfWords if word]
    FinalList=[]
    for i in ListOfWords2:
        if i not in FinalList:
            # print(i)
            FinalList.append(i)
    print(len(FinalList))
else:
    print(0)