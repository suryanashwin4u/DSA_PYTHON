# A number N is given. Divide it in half by using the binary shift operator.
# Use the floor value if the result is in decimal. 
# If the number is 1, leave it as it is.

#User function Template for python3

class Solution:
    def half(self, N):
        if N == 1:
            return 1
        return N >> 1
