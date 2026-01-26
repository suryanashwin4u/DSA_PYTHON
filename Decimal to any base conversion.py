# Given a decimal number N and the base B to which it should be converted. 
# Convert the given number to the given base.

class Solution:
    def getNumber(self, B, N):
        # Characters to represent digits beyond 9 (A–F for base up to 16)
        digits = "0123456789ABCDEF"
        
        # If N is 0, directly return "0"
        if N == 0:
            return "0"
        
        result = ""
        
        # Convert decimal N to base B
        while N > 0:
            rem = N % B                  # Get remainder
            result = digits[rem] + result  # Map remainder to character
            N = N // B                  # Reduce N
        
        return result