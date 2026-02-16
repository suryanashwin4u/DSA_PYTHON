# Given a N X N binary Square Matrix where each row 
# and column of the matrix is sorted in ascending order. 
# Find the total number of zeros present in the matrix.

class Solution:
    def countZeroes(self, A, N):
        count = 0
        
        for i in range(N):
            for j in range(N):
                if A[i][j] == 0:
                    count += 1
                    
        return count