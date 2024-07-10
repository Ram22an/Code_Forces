NumPro,TimeTrav=map(int,input().split())
TimeSpent=0
counter=0
for i in range(1,NumPro+1):
    TimeSpent=TimeSpent+i*5
    if TimeSpent+TimeTrav<=240:
        counter=i
print(counter)
