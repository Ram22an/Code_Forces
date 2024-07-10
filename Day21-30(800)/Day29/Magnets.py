NumberOFMagnets=int(input())
arr=[]
GroupCount=1
temp=input()
for i in range(1,NumberOFMagnets):
    temp2=input()
    if temp2!=temp:
        GroupCount+=1
        temp=temp2
print(GroupCount)

# this is new approach for this question
# i haven't created any array i have just used the input and compare with the current input
# if equal to previous input then continue but not equal to it then increment the group count
# and swap the value of pervious value
