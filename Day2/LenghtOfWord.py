num=int(input())
arr=[]*num
for i in range(num) :
    word=input()
    if 10<len(word):
        arr.append(word[0]+str(len(word)-2)+word[-1])
    else:
        arr.append(word)
for i in arr:
    print(i)