Num=int(input())
Stones=input()
StoneTOBeRemoved=0
if len(Stones)>1:
    for i in range(1,len(Stones)):
        if Stones[i-1]==Stones[i]:
            StoneTOBeRemoved+=1
    print(StoneTOBeRemoved)
else:
    print(0)
# it was not looking easy ny reading the question but we have to use simple looping as i was thinking
# but i learned about new type of looping here start from 1 and compare the next one 
