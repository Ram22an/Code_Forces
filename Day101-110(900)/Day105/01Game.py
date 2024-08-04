x=int(input())
for _ in range(x):
    num=input()
    countof1=num.count("1")
    countof0=num.count("0")
    Val=min(countof0,countof1)
    if Val%2==0:
        print("NET")
    else:
        print("DA")
# it was easy problem
