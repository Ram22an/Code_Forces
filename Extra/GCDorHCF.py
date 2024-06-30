Num1=int(input())
Num2=int(input())
# this will run for O(min(num1,num2))
# if Num1%Num2==0 :
#     print(Num2)
# elif Num2%Num1==0:
#     print(Num1) 
# else:
#     counter=0
#     MinVal=Num1 if Num1<Num2 else Num2
#     while MinVal>0:
#         if Num1%MinVal==0 and Num2%MinVal==0:
#             counter=1
#             print(MinVal)
#             break
#         MinVal-=1
#     if counter==0:
#         print(1)




# this is Euclidean algo
# this will run for  O(logmin(Num1,Num2)) 
# for example num1=15 and num2=12 we know answer is 3
# it will check in while loop that is num1 and num2 are not equal if not it will proceed
# it will find the smallest number from them 
# it will subtract small number from larger number 
# this is will make both number equal to the hcf of both number 

# while Num1!=Num2:
#     if Num1>Num2:
#         Num1-=Num2
#     else:
#         Num2-=Num1
# print(Num1)





# here is the more optimized Euclidean algo with recursion
# num1=12 and num2=15 

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(Num1,Num2))
