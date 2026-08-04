# Given two matrices mat1[][] and mat2[][] of size (4x4). 
# Find whether the resultant res[][] matrix is equal to the multiplication of both the matrices.

class Solution:
    def multiplyMatrix(self, mat1, mat2, result):
        # iterate rows
        for i in range(4):
            # iterate columns
            for j in range(4):
                sum_val = 0
                
                # multiplication and sum
                for k in range(4):
                    sum_val += mat1[i][k] * mat2[k][j]
                
                # compare with given result
                if sum_val != result[i][j]:
                    return False
                
        return True
