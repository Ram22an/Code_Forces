Sentence=input()
Counter=False
for i in Sentence:
    if ord(i)==72 or ord(i)==81 or ord(i)==57:
        Counter=True
        break
if Counter:
    print("YES")
else:
    print("NO")
# please read the question carefully
