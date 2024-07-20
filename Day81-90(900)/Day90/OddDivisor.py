def has_odd_divisor(n):
    # in this loop we are checking if the number is even or odd
    # if it satisfies the condition then it moves 
    while n % 2 == 0:
        # here we are checking if we divide the number and get the number 
        # which matched the condition above 
        n =n// 2
    return n > 1
    # example suppose we have n=6
    # first entry in loop we have 6%2==0 i.e. true
    # then it moves to inside then it give 6//2=3 which is not divisible by 
    # conclusion is we are checking if the number is in the power of 2 and in exactly in power of 2
    # if it is not exactly then it is divisible by odd number and odd nubmer could be any odd nubmer
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if has_odd_divisor(n):
        print("YES")
    else:
        print("NO")
# it was easy question by coding but by observation is required good level of observation
