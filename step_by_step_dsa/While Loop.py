# Given a number n, print all numbers from 0 to n in increasing order in a single line using a while loop.
# Expected Complexities
# Time Complexity: O(n)
# Auxiliary Space: O(1)


n = int(input())
i = 0
# code here
while i<=n:
    print(i,end=' ')
    i=i+1