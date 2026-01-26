# You are given two square matrices, a[][] and b[][], each of size n x n. 
# Your task is to compute the sum of these two matrices and store the result in the matrix a[][] itself.

class Solution:
    def Addition(self, matrixA, matrixB):
        # Get number of rows (n x n matrix)
        n = len(matrixA)
        
        # Traverse each row
        for i in range(n):
            # Traverse each column
            for j in range(n):
                # Add corresponding elements of both matrices
                matrixA[i][j] += matrixB[i][j]
        
        # No return needed as result is stored in matrixA itself