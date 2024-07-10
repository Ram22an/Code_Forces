PriceOfOne,Money,NoOfBananas=map(int,input().split())
# Sum=NoOfBananas*(NoOfBananas+1)/2
Sum=NoOfBananas*(PriceOfOne*NoOfBananas+PriceOfOne)/2
if Sum>Money:
    print(int(Sum-Money))
else:
    print(0)
# the only problem i was facing in this was i not considering that is money is more than sum 
# thats why i was getting negative value when i was doing sum-total
