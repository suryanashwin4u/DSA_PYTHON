# Given an integer array arr, 
# return all the unique pairs [arr[i], arr[j]] 
# such that i != j and arr[i] + arr[j] == 0.
# Expected Time Complexity: O(n log n)
# Expected Auxiliary Space: O(n).

class Solution:
    def getPairs(self, arr):
        arr.sort()
        n = len(arr)
        left, right = 0, n - 1
        result = []

        while left < right:
            s = arr[left] + arr[right]

            if s == 0:
                result.append([arr[left], arr[right]])

                # skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1

        return result