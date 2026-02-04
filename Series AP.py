# Given the first 2 terms a1 and a2 of an Arithmetic Series. 
# Find the nth term of the series. 

class Solution:
    def nthTermOfAP(self, a1: int, a2: int, n: int) -> int:
        """
        This function returns the nth term of an Arithmetic Progression (AP)
        
        a1 -> first term of AP
        a2 -> second term of AP
        n  -> term number to find
        """

        # Step 1: Calculate the common difference
        # Common difference = second term - first term
        d = a2 - a1

        # Step 2: Apply the formula for nth term of AP
        # nth term = a1 + (n - 1) * d
        nth_term = a1 + (n - 1) * d

        # Step 3: Return the result
        return nth_term
