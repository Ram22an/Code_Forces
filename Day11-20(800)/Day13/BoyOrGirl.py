username=input()
arr=[]
for i in username:
    if i not in arr:
        arr.append(i)
if len(arr)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")