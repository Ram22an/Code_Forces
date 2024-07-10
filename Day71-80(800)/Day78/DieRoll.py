import math
Y,W=map(int,input().split())
MaxAmount=max(Y,W)
Numerator=7-MaxAmount
Denominator=6
if Numerator==Denominator:
    print("1/1")
elif Numerator==1:
    pass
# here is the corrected code 
def probability_to_visit_transylvania(Y, W):
    MaxAmount = max(Y, W)
    Numerator = 7 - MaxAmount
    Denominator = 6
    
    gcd = math.gcd(Numerator, Denominator)
    Numerator //= gcd
    Denominator //= gcd
    
    return f"{Numerator}/{Denominator}"
Y, W = map(int, input().split())
print(probability_to_visit_transylvania(Y, W))
