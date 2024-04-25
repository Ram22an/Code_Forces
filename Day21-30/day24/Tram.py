NumberOfStops=int(input())
Total=0
Max=0
for i in range(NumberOfStops):
    OutPass,InPass=map(int,input().split())
    Total=InPass-OutPass+Total
    if Max<Total:
        Max=Total
print(Max)


# I have told you Do not alway go for array and looping 
# you are an idiot it was simple question