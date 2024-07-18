Children,Puzzles=map(int,input().split())
ListOfPuzzles=list(map(int,input().split()))
ListOfPuzzles.sort()
# we are getting a large number 
MinDiff=float('inf')
# ensures that we iterate through all possible starting points for segments of length n. Here, 
# Puzzles - Children + 1 is 7 - 3 + 1 = 5, 
# so i will range from 0 to 4.
for i in range(Puzzles-Children+1):
    # it will go form [0+3-1] i.e. 2,3,4,5,6 and other will we 0,1,2,3,4
    current=ListOfPuzzles[i+Children-1]-ListOfPuzzles[i]
    if current<MinDiff:
        MinDiff=current
print(MinDiff)
