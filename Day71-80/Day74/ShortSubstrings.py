x=int(input())
for _ in range(x):
    Word=list(map(str,input()))
    i=2
    Final=""
    while i<len(Word):
        if i%2==0:
            Word[i]=0
        i+=1
    for i in Word:
        if i!=0:
            Final+=i
    print(Final)
