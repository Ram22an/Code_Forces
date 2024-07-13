
# Range,Index=map(int,input().split())
# Odd=[]
# Even=[]
# for i in range(1,Range+1):
#     if i%2==0:
#         Even.append(i)
#     else:
#         Odd.append(i)
# Result=Odd+Even
# print(Result[Index-1])
# here is my approach which is correct for small n but here is the constraint it is goin to 10^12 which is not small

n, k = map(int, input().split())
# count of even number in a series of n number is n//2
# count of odd number in a series of n number is (n+1)//2
number_of_odds = (n + 1) // 2
# number_of_even=n//2
# why we are only considering number of odd number because we want to know that where k is lying
# like in which side 
# print(number_of_odds,number_of_even)
if k <= number_of_odds:
    # this is formula for kth odd number like odd number starts from 1,3,5,7,9... to find second or "2" odd number
    # 2*2-1=4-1 i.e. is 3 and it is correct
    result = 2 * k - 1
else:
    # the formula to find kth even number is 2*k the series of even number starts with 2,4,6,8,10... to find second even number
    # 2*2=4 and it is correct  
    result = 2 * (k - number_of_odds)
    # here we are doing k - number_of_odds because when k is bigger than number of odd numbers then we have find the position of
    # even number starting from 2 suppose we have used two array before odd=[] and even=[] suppose we are doing this for 7
    # then we are having odd=[1,3,5,7] and even=[2,4,6] then we have to give 7 element of this array(odd+even)
    #  [1,3,5,7,2,4,6] so number of odd number are here 4 so when we do 7-4 i.e. 3 so third even number is 2*3 that is 6 and answer is also 6
print(result)
# it is an easy but conceptual question
