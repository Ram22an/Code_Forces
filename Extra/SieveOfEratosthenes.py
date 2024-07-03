# def PrimeOrNot(Num):
#     if Num==1:
#         return False
#     if Num ==2 or Num==3:
#         return True
#     if Num%2==0 or Num%3==0:
#         return False
#     for i in range(5,int(Num**0.5)+1,6):
#         if Num%i==0 or Num%(i+2)==0:
#             return False
#     return True
def SieveOfEratosthenes(Num):
    Arr=[True]*(Num+1)
    Arr[0]=False
    Arr[1]=False
    if Num<=1:
        return print("It is one or 0")
    print("|| ",end="")
    for i in range(2,int(Num**0.5)+1,1):
        if Arr[i]:
            # print(i,end=" || ")
            # before it is i*2 
            # the written is more optimized
            for j in range(i*i,Num+1,i):
                Arr[j]=False
 
    for i in range(Num+1):
        if Arr[i] :
            print(i,end=" || ")

if __name__=="__main__":
    x=int(input())
    SieveOfEratosthenes(x)
