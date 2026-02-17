# Given an array, the task is to 
# find the difference between the highest occurrence and lowest occurrence of any number in an array.
# Note: If only one type of element is present in the array return 0

class Solution:
    def findDiff(self, arr):
        freq = {}

        # Count frequency
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Get max and min frequency
        max_freq = max(freq.values())
        min_freq = min(freq.values())

        return max_freq - min_freq
