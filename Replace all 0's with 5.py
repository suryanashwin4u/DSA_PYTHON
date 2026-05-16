# You are given an integer n. 
# You need to convert all zeroes of n to 5.

# Time Complexity: O(k)
# Auxiliary Space: O(1)

class Solution:
    def convertFive(self, n):
        return int(str(n).replace('0', '5'))

# or

class Solution:
    def convertFive(self, n):
        
        if n == 0:
            return 5
            
        result = 0
        place = 1
        
        while n > 0:
            digit = n % 10
            
            if digit == 0:
                digit = 5
                
            result = digit * place + result
            place *= 10
            n //= 10
            
        return result