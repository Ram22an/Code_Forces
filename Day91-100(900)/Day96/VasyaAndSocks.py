socks,Day=map(int,input().split())
counter=0
i=0
while socks!=0:
    if i%Day==0:
      socks+=1
    counter+=1
    socks-=1
    i+=1
print(counter-1) 
# it was easy problem
