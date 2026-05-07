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

        # Step 1: Find candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        # Step 2: Verify candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate

        return -1