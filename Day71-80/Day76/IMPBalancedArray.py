x=int(input())
for _ in range(x):
    Num=int(input())
    if Num%4!=0:
        print("NO")
        continue
    EvenArry = []
    OddArry = []
    EvenSum = 0
    OddSum = 0
    i = 1

    while len(EvenArry) < Num // 2:
        if i % 2 == 0:
            EvenArry.append(i)
            EvenSum += i
        i+= 1
    i=1
    while len(OddArry) < Num // 2 - 1:
        if i % 2 != 0:
            OddArry.append(i)
            OddSum += i
        i += 1
    OddArry.append(EvenSum - OddSum)
    print("YES")
    print(" ".join(map(str, EvenArry + OddArry)))

    # EvenArry=[]
    # OddArry=[]
    # EvenSum=0
    # OddSum=0
    # i=1
    # while True:
    #     if i % 2 == 0 and i not in OddArry:
    #         EvenArry.append(i)
    #         EvenSum+=i
    #     elif i%2!=0 and i not in EvenArry:
    #         OddArry.append(i)
    #         OddSum+=i
    #     if len(EvenArry)==Num//2 and len(OddArry)==Num//2:
    #         if EvenSum==OddSum:
    #             print("YES")
    #             print("".join(map(str,EvenArry)))
    #         else:
    #             print(EvenArry,OddArry)
    #             print("NO")
    #             break
    #     i+=1
# it is good question try it to remember it 
# since we have to make array of size n/2 not of n 
# sum of even numbers is n(n+1) and of odd it is n^2
#  so n/2(n/2+1)=(n^2)/4 but there is small cahnge as we know interval is of 2 so formula is 
# n/2(n/2+2)=(n^2)/4
# for even
# S= n/2×(first term+last term)
# S(odd)=n^2
# so after solving this we got n=4 
# so the number with multiple of 4 can make the array
