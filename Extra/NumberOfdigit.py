x=int(input())
counter=0
while x>0:
    counter+=1
    x=int(x/10)
    # or x=x//10
print(counter)