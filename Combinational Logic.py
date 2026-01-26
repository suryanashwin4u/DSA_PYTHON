# Construct a 6 input gate which performs the following logical operation:
#  (not(A)).B + C.D +E.(not(F))
# where A, B, C, D, E and F are the inputs to the 6 input gate.

class Solution:
    def logicalOperation(self, A, B, C, D, E, F):
        # Compute (not A) and B
        term1 = (not A) and B
        
        # Compute C and D
        term2 = C and D
        
        # Compute E and (not F)
        term3 = E and (not F)
        
        # OR all three terms
        result = term1 or term2 or term3
        
        # Convert boolean result to integer (0 or 1)
        return int(result)