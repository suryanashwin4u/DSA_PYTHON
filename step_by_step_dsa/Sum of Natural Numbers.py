# Given an integer n, compute the sum of all natural numbers from 1 to n (inclusive). 
# If n is 0, the sum should be 0.

# Expected Complexities
# Time Complexity: O(1)
# Auxiliary Space: O(1)

n = int(input())
sum = 0
sum = int(n*(n+1)/2)
print(sum)