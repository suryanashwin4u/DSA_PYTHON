class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        repeating = missing = 0

        # Step 1: Mark visited numbers
        for i in range(n):
            idx = abs(arr[i]) - 1   # correct index
            if arr[idx] < 0:
                repeating = abs(arr[i])
            else:
                arr[idx] = -arr[idx]

        # Step 2: Find missing number
        for i in range(n):
            if arr[i] > 0:
                missing = i + 1
                break

        return [repeating, missing]
