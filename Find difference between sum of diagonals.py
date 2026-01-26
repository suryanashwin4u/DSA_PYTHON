# Given a matrix Grid[][] of size NxN. 
# Calculate the absolute difference between the sums of its diagonals

class Solution:
    def diagonalSumDifference(self, N, Grid):
        # Sum of primary diagonal
        primary_sum = 0
        
        # Sum of secondary diagonal
        secondary_sum = 0
        
        # Loop through rows
        for i in range(N):
            # Primary diagonal element: Grid[i][i]
            primary_sum += Grid[i][i]
            
            # Secondary diagonal element: Grid[i][N - i - 1]
            secondary_sum += Grid[i][N - i - 1]
        
        # Return absolute difference
        return abs(primary_sum - secondary_sum)