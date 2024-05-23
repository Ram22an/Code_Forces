x=int(input())
a=x
Nx=0
while x>0:
    Nx=Nx*10+x%10
    x=x//10
# print(Nx)
if a==Nx:
    print("Yes")
else:
    print("NO")
