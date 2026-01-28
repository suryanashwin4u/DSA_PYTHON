# For a given number N. 
# Print the pattern in the following form: 
# 1 121 12321 1234321 for N = 4.

class Solution:
    def numberPattern(self, N):
        result = []                     # list to store all pattern strings
        
        for i in range(1, N + 1):       # rows from 1 to N
            row = ""
            
            # increasing part: 1 to i
            for j in range(1, i + 1):
                row += str(j)
            
            # decreasing part: i-1 to 1
            for j in range(i - 1, 0, -1):
                row += str(j)
            
            result.append(row)          # add row to result list
                    
        return result