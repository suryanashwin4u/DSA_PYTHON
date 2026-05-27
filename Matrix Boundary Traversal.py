# You are given a matrix mat[][] . 
# Return the boundary traversal on the matrix in a clockwise manner 
# starting from the first row of the matrix.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def boundaryTraversal(self, mat):

        n = len(mat)
        m = len(mat[0])

        ans = []

        # single row
        if n == 1:
            return mat[0]

        # single column
        if m == 1:
            return [mat[i][0] for i in range(n)]

        # top row
        for j in range(m):
            ans.append(mat[0][j])

        # right column
        for i in range(1, n):
            ans.append(mat[i][m - 1])

        # bottom row
        for j in range(m - 2, -1, -1):
            ans.append(mat[n - 1][j])

        # left column
        for i in range(n - 2, 0, -1):
            ans.append(mat[i][0])

        return ans