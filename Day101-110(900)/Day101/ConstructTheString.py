import random
Arr= [chr(i) for i in range(97, 122 + 1)]
t=int(input())
for _ in range(t):
    Size,SubString,Distinct=map(int,input().split())
    # Create a base pattern of length `SubString` with exactly `Distinct` distinct letters
    base_pattern = ''.join(Arr[:Distinct])
    # base_patter created to have exactly Distinct distinct letters.
    base_pattern = (base_pattern * ((SubString // Distinct) + 1))[:SubString]
    # above we are multiplying the string number of times we need and then slicing it to the substring size
    Ans = ""
    # here we are simply adding the base pattern to the answer 
    for _ in range(Size // SubString):
        Ans += base_pattern
    remaining = Size % SubString
    if remaining > 0:
        Ans += base_pattern[:remaining]
    print(Ans)
# this question is very hard i tried to do it with different appraoch but it didn't work 
# this is the code with i was able to understand
