# Given an array Arr[] of N integers.
# Find the sum of values of even and odd index positions separately.

class Solution:
    def EvenOddSum(self, N, Arr):
        # Initialize sums
        even_sum = 0   # for even index positions (0-based)
        odd_sum = 0    # for odd index positions (0-based)

        # Traverse the array
        for i in range(N):
            if i % 2 == 0:        # even index
                even_sum += Arr[i]
            else:                 # odd index
                odd_sum += Arr[i]

        # Return result as per GFG format
        return [even_sum, odd_sum]