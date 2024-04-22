Word=input()
# Number=int(Word)
CountOf7=Word.count("7")
CountOf4=Word.count("4")
total=CountOf7+CountOf4
if total==4 or total==7:
    print("YES")
else:
    print("NO")