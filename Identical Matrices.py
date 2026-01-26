# Given two square matrices Grid1 and Grid2 with the same dimensions(NxN).
# Check whether they are identical or not.

class Solution:
    def areMatricesidentical(self, N, Grid1, Grid2):
        # Traverse each row
        for i in range(N):
            # Traverse each column
            for j in range(N):
                # If any element differs, matrices are NOT identical
                if Grid1[i][j] != Grid2[i][j]:
                    return 0
        
        # If all elements matched
        return 1