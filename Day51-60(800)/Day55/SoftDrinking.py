Friends,NumsSoftDrink,Milliliters,Limes,Slice,Salt,NeedMl,NeedSalt=map(int,input().split())
PerPerson=(NumsSoftDrink*Milliliters)//(NeedMl*Friends)
TotalLimes=(Limes*Slice)//Friends
TotalSalt=Salt//(NeedSalt*Friends)
print(int(min(PerPerson,TotalLimes,TotalSalt)))
