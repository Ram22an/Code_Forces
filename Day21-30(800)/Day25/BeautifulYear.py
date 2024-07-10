Year=int(input())
AnotherYear=Year+1
while True:
    FourthDigit=int(AnotherYear/1000)
    ThirdDigit=int(AnotherYear/100)%10
    SecondDigit=int(AnotherYear/10)%10
    FirstDigit=int(AnotherYear%10)
    # print(FourthDigit,ThirdDigit,SecondDigit,FirstDigit)
    if AnotherYear>Year and FourthDigit!=FirstDigit and FourthDigit!=SecondDigit and FourthDigit!=ThirdDigit and ThirdDigit!=FirstDigit and ThirdDigit!=SecondDigit and SecondDigit!=FirstDigit:
        print(AnotherYear)
        break
    else:
        AnotherYear+=1

# This we can find the every digit of number first i was finding all the digit by brute force which is not good
# print(int(AnotherYear/1000))
# print(int(AnotherYear/100)%10)
# print(int(AnotherYear/10)%10)
# print(int(AnotherYear%10))