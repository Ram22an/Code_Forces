Time=int(input())
Games=input()
Anton=Games.count("A")
Danik=Games.count("D")
if Anton>Danik:
    print("Anton")
elif Danik>Anton:
    print("Danik")
else:
    print("Friendship")