# this is real answer please check below
word1=input()
word2=input()
word1=word1.lower()
word2=word2.lower()
if word1>word2:
    print(1)
elif word2>word1:
    print(-1)
else:
    print(0)


# ans=len(word1)
# for i in range(len(word1)):
#     if ord(word1[i])<ord(word2[i]):
#         ans=ans-1
#     elif ord(word1[i])>ord(word2[i]):
#         ans=ans+1
#     else:
#         ans=ans
# if ans<len(word1):
#     print(-1)
# elif ans>len(word1):
#     print(1)
# else:
#     print(0)
# ////////////////////////////////////////////////////////////////////////////////////////////////
# this was my approach i don't know why it was failing 
word1=input()
word2=input()
word1=word1.lower()
word2=word2.lower()
ans=len(word1)
print(len(word1))
for i in range(len(word1)):
    if ord(word1[i])<ord(word2[i]):
        ans=ans-1
        print(-1)
    elif ord(word1[i])>ord(word2[i]):
        ans=ans+1
        print(1)
    else:
        print(0)
print("Answer is "+str(ans-len(word1)))