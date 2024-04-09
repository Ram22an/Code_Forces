import math as m
x=int(input())
for i in range(x):
    house,NumApt=map(int,input().split())
    if house<=2:
        print(1)
    else:
        house=house-2
        answ=m.ceil(house/NumApt)
        # answ2=m.floor(house/NumApt)
        print(answ+1)
        # print(answ2+2)
        # print(house/NumApt)
# in this we have learned about ciel function in math
# in this we have given house number and house on per floor and 
# there we are dividing house number -2 (Because first floor have 2 house) with number of number of house per floor
# here we are taking ciel value because we know floor can't have house in fraction
# we are taking ciel not floor because by taking floor we can miss one house or more than one 
# if house / numApt ==x.0 or it is fully divisible than we have to add one only other wise 2