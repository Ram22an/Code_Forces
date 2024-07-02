# Arr=["c","o","d","e","f","o","r","c","e","s"]
Arr=list(map(str,"codeforces"))
# print(Arr)
x=int(input())
for _ in range(x):
    StrVar=input()
    if StrVar in Arr:
        print("YES")
    else:
        print("NO")
