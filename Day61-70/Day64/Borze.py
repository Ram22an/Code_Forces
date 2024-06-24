Code=input()
i=0
Ans=""
while i < len(Code):
    if Code[i] == ".":
        Ans += "0"
        i += 1
    elif Code[i] == "-":
        if i + 1 < len(Code) and Code[i + 1] == ".":
            Ans += "1"
            i += 2
        elif i + 1 < len(Code) and Code[i + 1] == "-":
            Ans += "2"
            i += 2
    else:
        i += 1
# Ans=""
# for i in range(0,len(Code)):
#     if Code[i]==".":
#         Ans+="0"
#     elif Code[i]=="-":
#         if i+1<len(Code) and Code[i+1]==".":
#             Ans+="1"
#             i+=2
#         elif i+1<len(Code) and Code[i+1]=="-":
#             Ans+="2"
#             i+=2
#         else:
#             i+=1
print(Ans)
Code = input()
Ans = ""
skip = False  # Flag to skip the next iteration

for i in range(len(Code)):
    if skip:
        skip = False
        continue
    
    if Code[i] == ".":
        Ans += "0"
    elif Code[i] == "-" and i + 1 < len(Code):
        if Code[i + 1] == ".":
            Ans += "1"
            skip = True
        elif Code[i + 1] == "-":
            Ans += "2"
            skip = True

print(Ans)
# here is the my approach with skip and moving to next character 
# it could be done with while loop easily but in for loop we have to 
# skip it with skip variable continue will restart the for loop
# for the next value of i
 