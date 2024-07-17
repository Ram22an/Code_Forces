# first appraoch
# Music=input().strip()
# i=0
# Ans=""
# while i<len(Music)-2:
#     if Music[i:i+3] != "WUB":
#         j=i
#         while j<len(Music)-2 and Music[j:j+3] != "WUB":
#             j+=1
#         Ans=Ans+" "+Music[i:j]
#         i=j
#     else:
#         i+=3
# if i < len(Music) and Music[i:i+3] != "WUB":
#     Ans += " " + Music[i:]
# print(Ans[1:])
# print(Ans.strip())
# Music = input().strip()
# words = Music.split("WUB")
# original_song = ' '.join(filter(None, words))
# print(original_song)

# The strip() method in Python is used to remove the whitespace or the characters that are passed in the argument. 
# The split() method, on the other hand, is used to split the string into substrings.
# take refernce from AntonAndLetters.py day42
# ListOfWords=re.split(r'[{ },]',Line)
    # here is the code implementation of re 
    # Trying=[]
    # for i in Line:
    #     if i==" " or i=='{' or i=='}' or i==',':
    #         Trying.append("")
    #     else:
    #         Trying.append(i)
    # print(Trying)
    # Trying2=[]
    # for i in Trying:
    #     if i!="":
    #         Trying2.append(i)
    # print(Trying2)
# second approach
# Music=input().strip()
# i=0
# while i<len(Music)-2:
#     if Music[i:i+3] == "WUB":
#         Music[i:i+3]=" "
#         i+=3
#     else:
#         i+=1
# print(Music)
Music = input().strip()
i = 0
while i < len(Music) - 2:
    if Music[i:i+3] == "WUB":
        Music = Music[:i] + " " + Music[i+3:]
    i += 1
print(" ".join(Music.split()))
# i tried this thing in my second appraoch and i don't know
# what is wrong with my first approach
