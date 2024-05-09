# here is the question try to understand it with test cases
# Given an array of N numbers and a positive integer K. 
# The problem is to find K numbers with the most occurrences,
# i.e., the top K numbers having the maximum frequency.
# If two numbers have the same frequency then the number with a larger value should be given preference
# The numbers should be displayed in decreasing order of their frequencies. 
# It is assumed that the array consists of at least K numbers'
# Examples: Input: arr[] = {3, 1, 4, 4, 5, 2, 6, 1}, K = 2 Output: 4 1 Explanation: Frequency of 4 = 2, Frequency of 1 = 2 These two have the maximum frequency and 4 is larger than 1
# Input: arr[] = {7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9}, K = 4 Output: 5 11 7 10 Explanation: Frequency of 5 = 3, Frequency of 11 = 2, Frequency of 7 = 2, Frequency of 10 = 1 These four have the maximum frequency and 5 is largest among rest


k=int(input())
arr=list(map(int,input().split()))
dic={}
for i in arr:
    if i not in dic: 
        dic[i]=1
    else:
        dic[i]=dic.get(i)+1
keys=list(dic.keys())
values=list(dic.values())
for i in range (0,len(keys)):
    for j in range(i+1,len(keys)):
        if keys[i]<keys[j]:
            temp=keys[i]
            keys[i]=keys[j]
            keys[j]=temp
            temp2=values[i]
            values[i]=values[j]
            values[j]=temp2
for i in range (0,len(keys)):
    for j in range(i+1,len(keys)):
        if values[i]<values[j]:
            temp=keys[i]
            keys[i]=keys[j]
            keys[j]=temp
            temp2=values[i]
            values[i]=values[j]
            values[j]=temp2
print(keys)
print(values)
for i in range(0,k):
    print(f"{keys[i]}-{values[i]}", end="\t")


# from collections import Counter

# # Input
# arr = list(map(int, input().split()))
# k = int(input())

# # Count the frequency of each element
# counter = Counter(arr)

# # Sort elements by frequency and then by value
# sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

# # Extract the keys and values
# keys = [item[0] for item in sorted_items]
# values = [item[1] for item in sorted_items]

# # Print the keys and values
# for i in range(min(k, len(keys))):
#     print(f"{keys[i]}-{values[i]}", end="\t")
