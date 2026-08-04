# Given an N bit binary number, 
# find the 1's complement of the number. 
# The ones' complement of a binary number is defined as 
# the value obtained by inverting all the bits in the 
# binary representation of the number 
# (swapping 0s for 1s and vice versa).

class Solution:
    def onesComplement(self, S, N):
        result = []
        
        # Traverse each bit in the string
        for bit in S:
            if bit == '0':
                result.append('1')
            else:
                result.append('0')
        
        # Convert list to string and return
        return ''.join(result)