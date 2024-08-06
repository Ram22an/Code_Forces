# To handle deep hierarchical structures, we increased the recursion limit 
import sys
sys.setrecursionlimit(3000)
# This function calculates the depth of the hierarchy for each employee recursively, 
# storing the result in the depth array.
def compute_depth(employee, managers, depth):
    if depth[employee] != -1:
        return depth[employee]
    
    if managers[employee] == -1:
        depth[employee] = 1
    else:
        depth[employee] = 1 + compute_depth(managers[employee] - 1, managers, depth)
    
    return depth[employee]
# This function initializes the depth array, iterates over each employee 
# to compute their depth, and keeps track of the maximum depth found.
def min_groups(n, managers):
    depth = [-1] * n
    
    max_depth = 0
    for i in range(n):
        max_depth = max(max_depth, compute_depth(i, managers, depth))
    
    return max_depth

# Input reading
n = int(input())
managers = []
for _ in range(n):
    managers.append(int(input()))

# Output the result
print(min_groups(n, managers))

# this question is out of my range so i copied it 
# now it is time to boost my dsa
