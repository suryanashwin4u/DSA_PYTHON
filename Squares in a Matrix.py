#Given a mxn matrix, count the number of squares in the matrix.

class Solution:
    def squaresInMatrix(self, m, n):
        total = 0
        limit = min(m, n)

        for i in range(1, limit + 1):
            total += (m - i + 1) * (n - i + 1)

        return total
