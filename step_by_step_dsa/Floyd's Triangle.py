# Given a number n, print Floyd's triangle with n lines.
# Floyd’s Triangle is a pattern of consecutive natural numbers arranged in rows, where the i-th row contains i numbers.

# Expected Complexities
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

class Solution:
    def printFloydTriangle(self, n):
        num = 1
        
        for i in range(1,n+1):
            for j in range(i):
                print(num,end=' ')
                num += 1
            print()