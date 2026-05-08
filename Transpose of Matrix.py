# You are given a square matrix of size n x n. 
# Your task is to find the transpose of the given matrix.
# The transpose of a matrix is obtained by converting all the rows to columns and all the columns to rows.
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

class Solution:
    def transpose(self, mat):
        n = len(mat)

        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

        return mat