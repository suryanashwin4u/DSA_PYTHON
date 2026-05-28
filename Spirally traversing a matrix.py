# You are given a rectangular matrix mat[][] of size n x m, 
# and your task is to return an array while traversing the matrix in spiral form.

# Time Complexity: O(n * m)
# Auxiliary Space: O(n * m)

class Solution:
    def spirallyTraverse(self, mat):
        
        top = 0
        bottom = len(mat) - 1
        
        left = 0
        right = len(mat[0]) - 1
        
        ans = []
        
        while top <= bottom and left <= right:
            
            # left -> right
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1
            
            # top -> bottom
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1
            
            # right -> left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1
            
            # bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1
        
        return ans

