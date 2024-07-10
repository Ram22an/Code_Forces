# this is my code and i have find more optimize approach
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    MinNum=min(a,b)
    MaxNum=max(a,b)
    Diff=MaxNum-MinNum
    counter=0
    counter=Diff//10+counter
    Diff=Diff%10
    counter=Diff//9+counter
    Diff=Diff%9
    counter=Diff//8+counter
    Diff=Diff%8
    counter=Diff//7+counter
    Diff=Diff%7
    counter=Diff//6+counter
    Diff=Diff%6
    counter=Diff//5+counter
    Diff=Diff%5
    counter=Diff//4+counter
    Diff=Diff%4
    counter=Diff//3+counter
    Diff=Diff%3
    counter=Diff//2+counter
    Diff=Diff%2
    counter=Diff//1+counter
    Diff=Diff%1
    print(counter)
# here is the more optimize approach
# It involves less donkey work
x = int(input())
for _ in range(x):
    a, b = map(int, input().split())
    Diff = abs(a - b)
    counter = 0
    
    for Nums in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        counter = Diff // Nums + counter
        Diff =Diff%Nums
    
    print(counter)
# both are correct but alway go for less donkey work
 