# Given an integer n, print a pyramid pattern of stars with n rows. 
# Each row consists of leading spaces followed by asterisks such that the stars are centered, 
# with the first row having 1 star and each subsequent row having 2 more stars than the previous row.

# Expected Complexities
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

class Solution:
  def printPyramid(self, n: int) -> None:
    for i in range(1, n + 1):
      spaces = " " * (n - i)
      stars = "*" * (2 * i - 1)
      print(spaces + stars)