NumberOfPeople,Time=map(int,input().split())
arr=list(input().strip())
Counter=[0]*NumberOfPeople
for i in range(Time):
    for j in range(1,NumberOfPeople):
        if arr[j-1]=='B' and arr[j]=='G' and Counter[j-1]<Time:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            Counter[j-1]+=1
            Counter[j-1],Counter[j]=Counter[j],Counter[j-1]
print("".join(arr))






# NumberOfPeople, Time = map(int, input().split())
# # strip takes an array and return a list based on field separator
# # and no argument mean none which really mean any whitspace
# arr = list(input().strip())
# # removes the whitspace from the edges and return the string 
# n = len(arr) // 2  # Calculate the number of rows
# two_d_arr = [[None, None] for _ in range(n)]  # Initialize the 2D array with None values

# # Fill the 2D array with pairs of characters
# for i in range(n):
#     two_d_arr[i][0] = arr[i*2]  # First column
#     two_d_arr[i][1] = arr[i*2 + 1]  # Second column

# print(two_d_arr)
# print(arr)
# for i in range(Time):
#     for j in range(1,len(arr)):
#         if arr[j-1]=='B' and arr[j]=='G':
#             arr[j-1]='G'
#             arr[j]='B'
# print(arr)

# # NumberOfPeople,Time=map(int,input().split())
# # arr=list(input().split())
# # print(arr)