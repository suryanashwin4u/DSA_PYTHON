# Given a number N, the task is to find the number of diagonals in N sided convex polygon.
class Solution:
    def diagonals(self, n):
        # Using formula: N * (N - 3) // 2
        # This gives number of diagonals in a convex polygon
        
        return n * (n - 3) // 2