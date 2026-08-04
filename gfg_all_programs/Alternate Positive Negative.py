# Given an unsorted array arr containing both positive and negative numbers. Your task is to rearrange the array and convert it into an array of alternate positive and negative numbers without changing the relative order.

# Note:
# - Resulting array should start with a positive integer (0 will also be considered as a positive integer).
# - If any of the positive or negative integers are exhausted, then add the remaining integers in the answer as it is by maintaining the relative order.
# - The array may or may not have the equal number of positive and negative integers.

class Solution:
    def rearrange(self, arr):
        # 1. Separate the numbers into two lists
        pos = [x for x in arr if x >= 0]
        neg = [x for x in arr if x < 0]
        
        i = j = k = 0
        
        # 2. Fill the original array with alternating values
        # We continue as long as both lists have elements left
        while i < len(pos) and j < len(neg):
            if k % 2 == 0:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1
            
        # 3. If positive numbers are left, append them
        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1
            
        # 4. If negative numbers are left, append them
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1