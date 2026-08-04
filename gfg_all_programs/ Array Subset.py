from collections import Counter

class Solution:
    def isSubset(self, a, b):
        """
        Checks whether array b is a subset of array a (duplicates allowed)
        
        Time Complexity:
        - Building frequency map of a: O(n)
        - Checking elements of b: O(m)
        - Total: O(n + m)
        
        Space Complexity:
        - Frequency map stores up to n elements
        - Total: O(n)
        """
        
        # Step 1: Count frequency of each element in array a
        freq = Counter(a)
        
        # Step 2: Check each element of array b
        for x in b:
            # If element not present or exhausted in a, b is not a subset
            if freq[x] == 0:
                return False
            
            # Reduce count after matching
            freq[x] -= 1
        
        # All elements of b found in a
        return True