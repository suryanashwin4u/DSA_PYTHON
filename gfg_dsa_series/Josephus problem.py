# You are playing a game with n people standing in a circle, numbered from 1 to n. 
# Starting from person 1, every kth person is eliminated in a circular fashion. 
# The process continues until only one person remains.
# Given integers n and k, return the position (1-based index) of the person who will survive.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def josephus(self, n: int, k: int) -> int:
        survivor = 0  # Base case for 1 person (0-indexed)
        
        # Build the solution bottom-up for 2 to n people
        for i in range(2, n + 1):
            survivor = (survivor + k) % i
            
        # Convert 0-based index to 1-based index
        return survivor + 1
    
# or

class Solution:
    def josephus(self, n: int, k: int) -> int:
        def solve(n, k):
            if n == 1:
                return 0
            return (solve(n - 1, k) + k) % n

        return solve(n, k) + 1