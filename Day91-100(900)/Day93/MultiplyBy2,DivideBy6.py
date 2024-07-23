# since 6 is composed of 2X3
# so if a number is is like x=2^n*3^m 
# if n and m are equal then if can we divible by 6 we have got
# another option that is multiply by 2 we can cahnge n but not m
def Number_of_Power_For_2(n):
    counter=0
    while n % 2 == 0:
        n =n// 2
        counter+=1
    return counter
def Number_of_Power_For_3(n):
    counter=0
    while n % 3 == 0:
        n =n// 3
        counter+=1
    return counter

x=int(input())
for _ in range(x):
    num=int(input())
    For2=Number_of_Power_For_2(num)
    For3=Number_of_Power_For_3(num)
    # if For2==For3 and num!=1:
    #     print(For2)
    # elif For2<For3:
    #     diff=For3-For2
    #     print(For3+diff)
    # elif For3<For2 :
    #     print(-1)
    # elif num==1:
    #     print(0)

    # it is used to determine if num has any prime factors other than 2 and 3
    remaining = num // (2 ** For2) // (3 ** For3)
    # remaining = num // ((2 ** For2) * (3 ** For3))
    print(For2,For3,remaining)
    if remaining != 1:
        print(-1)
    elif num == 1:
        print(0)
    elif For2 > For3:
        print(-1)
    else:
        print(2 * For3 - For2)
# it is confirmed that is is correct or not
