# Given a 2D integer matrix mat[][] of size n x m, 
# where every row and column is sorted in increasing order and a number x, 
# the task is to find whether element x is present in the matrix.

#User function Template for python3

class Solution:
    def matSearch(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Start from top-right corner
        row = 0
        col = m - 1
        
        while row < n and col >= 0:
            
            if mat[row][col] == x:
                return True
            
            elif mat[row][col] > x:
                col -= 1   # move left
            
            else:
                row += 1   # move down
        
        return False