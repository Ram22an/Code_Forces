Columns=int(input())
ColArray=list(map(int,input().split()))
ColArray.sort()
print(" ".join(map(str,ColArray)))
# this question looks so difficult but it is easy
# when the gravity is down we have given the configuration of toy cubes
# then gravity changes and it shiftes to the right and than all tha cubes starts to move right
# so they will arrange them self in ascending order
