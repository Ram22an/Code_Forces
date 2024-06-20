# this was my approach it was correct but the n (2 ≤ n ≤ 2·10^18)
# with this program it was exceeding the time limit
Power=int(input())
Temp=5**Power
Anws=Temp%100
print(Anws)
#  since i forgot that if we do 5^x the last 2 digit will be 25 is x is equal or greater then 2
# else it will be only one case when x=1 where it is 5
Power = int(input())
if Power >= 2:
    print("25")
else:
    print("5")
# it the solution in constant time
