word=input()
lower,upper=0,0
for i in word:
    if 65<=ord(i) and ord(i)<=90:
        upper+=1
    if 97<=ord(i) and ord(i)<=122:
        lower+=1
if upper<=lower:
    print(word.lower())
else:
    print(word.upper())