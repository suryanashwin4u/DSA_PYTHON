# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
# Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

class Solution:
    def checkEqual(self, a, b) -> bool:
        # If lengths are different, arrays can never be equal
        if len(a) != len(b):
            return False

        # Dictionary to store frequency of elements in array a
        freq = {}

        # Count frequency of each element in array a
        for num in a:
            freq[num] = freq.get(num, 0) + 1

        # Decrease frequency using elements from array b
        for num in b:
            # If element not found or frequency becomes negative, not equal
            if num not in freq:
                return False
            freq[num] -= 1

        # Check if all frequencies are zero
        for count in freq.values():
            if count != 0:
                return False

        return True