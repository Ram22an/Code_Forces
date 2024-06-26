x=int(input())
for _ in range(x):
    Rating=int(input())
    if 1900<=Rating:
        print("Division 1")
    elif 1600<=Rating<=1899:
        print("Division 2")
    elif 1400<=Rating<=1599:
        print("Division 3")
    elif Rating<=1399:
        print("Division 4")
