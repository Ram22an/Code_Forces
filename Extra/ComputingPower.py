# Naive approach
def ComputingPower(Num,Power):
    x=1
    for i in range(Power):
        x=x*Num
    print(x)
# def ComputingPowerRecursive(Num,Power):
#     if Power==0:
#         return 1
#     temp=ComputingPowerRecusive(Num,Power//2)
#     temp=temp*temp
#     if temp%2==0:
#         return temp
#     else:
#         return temp*Num
def ComputingPowerRecursive(Num, Power):
    if Power == 0:
        return 1
    temp = ComputingPowerRecursive(Num, Power // 2)
    temp = temp * temp
    if Power % 2 != 0:
        temp = temp * Num
    return temp

if __name__=="__main__":
    Num,Power=map(int,input().split())
    Power=ComputingPowerRecursive(Num,Power)
    print(Power)
