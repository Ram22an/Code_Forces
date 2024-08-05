x=int(input())
for _ in range(x):
    Health,Absorbe,Lighting=map(int,input().split())
    # here we are checking Health is > 20 beacuse absorbe is
    # more effective when it is more effective because it adds divides it by 2 and then add 10
    while Absorbe > 0 and Health > 20:
        Health = (Health // 2) + 10
        Absorbe-= 1
    Health-=10*Lighting
    if Health<=0:
        print("YES") 
    else:
        print("NO")
# it was good question but we have to observe question more carefully
