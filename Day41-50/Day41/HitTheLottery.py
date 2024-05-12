Money=int(input())
total=0
total=total+int(Money/100)
Money=Money%100
# print(total) 
# print(Money)
total=total+int(Money/20)
Money=Money%20
# print(total)
# print(Money)
total=total+int(Money/10)
Money=Money%10
# print(total)
# print(Money)
total=total+int(Money/5)
Money=Money%5
# print(total)
# print(Money)
total=total+int(Money/1)
Money=Money%1
# print(total)
# print(Money)
print(int(total))