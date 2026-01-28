# Given a square matrix of size n×n. 
# Your task is to calculate the sum of its diagonals.

class Solution:
    def DiagonalSum(self, matrix):
        n = len(matrix)
        total = 0
        
        for i in range(n):
            total += matrix[i][i]           # primary diagonal
            total += matrix[i][n - i - 1]   # secondary diagonal
        
        return total