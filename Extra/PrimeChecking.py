# it is naive method it have time complexity is O(n)
Num=int(input())
if Num==1:
    print("False")
else:
    counter=0
    for i in range(2,Num):
        if Num%i==0:
            print("False")
            counter=0
            break
        else:
            counter=1
    if counter==1:
        print("True")
# here is the another approach 
x=int(input())
if Num==1:
    print("False")
else:
    