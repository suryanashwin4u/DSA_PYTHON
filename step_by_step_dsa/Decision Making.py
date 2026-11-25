# Given two integers, n and m. 
# The task is to check the relation between n and m. 
# Print "less" if n < m,  "equal" if n == m, and "greater" if n > m.

# Expected Complexities
# Time Complexity: O(1)
# Auxiliary Space: O(1)

n = int(input())
m = int(input())

# code here
if n<m:
    print("less")

if n==m:
    print("equal")
    
if n>m:
    print("greater")