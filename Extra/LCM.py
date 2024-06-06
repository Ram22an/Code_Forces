a=int(input())
b=int(input())
if a%b==0:
    print(a)
elif b%a==0:
    print(b)
else:
    counter=0
    val=a*b
    minVal=min(a,b)
    for i in range(minVal,val):
        if i%a==0 and i%b==0:
            counter=1
            print(i)
            break
    if counter==0:
        print(val)