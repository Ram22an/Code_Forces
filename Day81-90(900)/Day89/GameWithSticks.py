n,m=map(int,input().split())
MinVal=min(n,m)
MinVal-=1
if MinVal%2==0:
    print("Akshat")
else:
    print("Malvika")
# This question looks difficult, but it is easy.
# Just go for the coordinates of the removed grids and eliminate the
# rows and columns, and it will always move diagonally.
