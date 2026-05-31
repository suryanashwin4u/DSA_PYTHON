# Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. 
# Return true if such a triplet exists, otherwise, return false.

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

class Solution:
    def findTriplets(self, arr):
        arr.sort()
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    return True

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return False