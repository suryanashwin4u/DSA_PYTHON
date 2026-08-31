# Given an array arr[]. 
# Find the majority element in the array. 
# If no majority element exists, return -1.

# Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0

        # Step 1: Find a potential majority candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Step 2: Verify if the candidate is actually the majority element
        freq = 0
        for num in arr:
            if num == candidate:
                freq += 1

        if freq > len(arr) // 2:
            return candidate

        return -1