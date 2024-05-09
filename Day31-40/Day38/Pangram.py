size=int(input())
word=input()
Alphabets=[0]*26
word=word.lower()
if size>=26:
    for i in word:
        Alphabets[ord(i)-97]=1
    if 0 in Alphabets:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
