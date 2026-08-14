# Given an unsorted array arr containing both positive and negative numbers. 
# Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

# Note:

# Resulting array should start with a positive integer (0 will also be considered as a positive integer).
# If any of the positive or negative integers are exhausted, 
# then add the remaining integers in the answer as it is by maintaining the relative order.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def rearrange(self, arr):
        # Separate positive (and zero) and negative integers
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        i = 0  # Pointer for pos array
        j = 0  # Pointer for neg array
        k = 0  # Pointer for original array arr
        
        # Interleave elements starting with positive
        while i < len(pos) and j < len(neg):
            if k % 2 == 0:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1
            
        # Add remaining positive integers if any
        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1
            
        # Add remaining negative integers if any
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1
            
        return arr