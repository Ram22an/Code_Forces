num1=input()
num1List=list(map(int,num1))
num2=input()
num2List=list(map(int,num2))
if len(num1)==len(num2):
    final=[]
    for i in range(len(num1)):
        if num1List[i]==num2List[i]:
            final.append(0)
        elif num1List[i]!=num2List[i]:
            final.append(1)
        
    print("".join(map(str,final)))
