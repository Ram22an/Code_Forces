NumberOfPeople=int(input())
arr=list(input().split())
try:
    for i in range (NumberOfPeople):
        if arr[i]=='1':
            print("HARD")
            break
    else:
        raise Exception('All elements are 0')
except Exception as e:
    print("EASY")
