# Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
# Find the maximum product that we can get in a subarray of arr[].

# Note: It is guaranteed that the answer fits in a 32-bit integer.

class Solution:
  def maxProduct(self, arr):
      n = len(arr)
      if n == 0:
          return 0

      # Initialize global max, current max, and current min with the first element
      max_so_far = arr[0]
      min_so_far = arr[0]
      result = arr[0]

      for i in range(1, n):
          curr = arr[i]

          # If current element is negative, swap max_so_far and min_so_far
          if curr < 0:
              max_so_far, min_so_far = min_so_far, max_so_far

          # Update max_so_far and min_so_far
          max_so_far = max(curr, max_so_far * curr)
          min_so_far = min(curr, min_so_far * curr)

          # Update the overall maximum product
          result = max(result, max_so_far)

      return result