Number=int(input())
total=0
if Number%2==0:
    total=int(Number/2)
else:
    total=int((Number+1)/2*-1)
print(total)

# in this we have logic like if number is even then its sum is n/2
# if it is odd then its sum is like (n+1)/2*-1
