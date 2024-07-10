num=int(input())
ans=""
for i in range(num):
    if i%2==0 and i<num-1:
        ans=ans+"I hate that "
    if i%2!=0 and i<num-1:
        ans=ans+"I love that "
    if i%2==0 and i==num-1:
        ans=ans+"I hate it "
    if i%2!=0 and i==num-1:
        ans=ans+"I love it "
print(ans)