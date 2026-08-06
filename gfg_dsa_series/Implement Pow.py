# Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).

# Time Complexity: O(log n)
# Auxiliary Space: O(log n)

class Solution:
    def power(self, b: float, e: int) -> float:
        # Handle negative exponent
        if e < 0:
            b = 1 / b
            e = -e
            
        ans = 1.0
        while e > 0:
            # If exponent is odd, multiply the base with the result
            if e % 2 == 1:
                ans *= b
            # Square the base and halve the exponent
            b *= b
            e //= 2
            
        return ans