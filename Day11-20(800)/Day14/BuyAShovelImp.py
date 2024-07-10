PricesOfOneShovel,Changes=map(int,input().split())
value=PricesOfOneShovel
# type(num) is int
counter=2
NoOfShovel=1
while True:     
    if  value%10==0:
        print(NoOfShovel)
        break
    if value%10==Changes:
        print(NoOfShovel)
        break
    value=counter*PricesOfOneShovel
    counter+=1
    NoOfShovel+=1
# here counte is started with 2 becuse if we start it with one it will check the price if it is 
# divisible by 10 or price%10 is equal to changes then if we multiply any number with 1 it will give the same result 
# but our no of shovel is incremented by one in each loop 