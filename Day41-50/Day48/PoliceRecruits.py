x=int(input())
Crime=list(map(int,input().split()))
CrimeOccured=0
PoliceAva=0
for i in Crime:
    if i!=-1:
        PoliceAva+=i
    else:
        if PoliceAva>0:
            PoliceAva-=1
        else:
            CrimeOccured+=1
print(CrimeOccured)


# this was my approach for first time
# x=int(input())
# Crime=list(map(int,input().split()))
# counter=0
# # finding last -1
# for i in range(x):
#     if Crime[i]==-1:
#         counter=i
# Crime2=Crime[:counter+1]
# Final=0
# for i in Crime2:
#     if i==-1:
#         Final+=1
#     else:
#         Final-=i
# if Final<0:
#     Final=0
# print(Final)
# Read input


# improved code 
# n = int(input())
# Crime = list(map(int, input().split()))

# # Find the index of the last crime (-1)
# last_crime_index = Crime.index(-1)

# # Calculate the number of untreated crimes
# untreated_crimes = 0
# available_officers = 0
# for i in range(last_crime_index + 1):
#     if Crime[i] == -1:
#         if available_officers > 0:
#             available_officers -= 1
#         else:
#             untreated_crimes += 1
#     else:
#         available_officers += Crime[i]

# # Print the number of untreated crimes
# print(untreated_crimes)
