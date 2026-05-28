# Given an array arr[], return true if there is a triplet (a, b, c) from the array (where a, b, and c are on different indexes) that satisfies a2 + b2 = c2, otherwise return false.

# Time Complexity: O(n + max(arr[i])^2)
# Auxiliary Space: O(max(arr[i]))

class Solution:
    def pythagoreanTriplet(self, arr):
        
        n = len(arr)

        # store squares
        squares = set()

        for num in arr:
            squares.add(num * num)

        # check all pairs
        for i in range(n):
            for j in range(i + 1, n):

                sum_sq = arr[i] * arr[i] + arr[j] * arr[j]

                if sum_sq in squares:
                    return True

        return False