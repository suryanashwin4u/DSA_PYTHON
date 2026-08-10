# You are given n disks placed on a starting rod (from), with the smallest disk on top and the largest at the bottom. There are three rods: the starting rod(from), the target rod (to), and an auxiliary rod (aux).
# You have to calculate the minimum number of moves required to transfer all n disks from the starting rod to the target rod, following these rules:
#       1. Only one disk can be moved at a time.
#       2. A disk can only be placed on top of a larger disk or on an empty rod.
# Return the minimum number of moves needed to complete the task.

# Time Complexity: O(2^n)
# Auxiliary Space: O(n)

class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        # Base case: 0 disks require 0 moves
        if n == 0:
            return 0
        
        # Base case: 1 disk takes 1 move
        if n == 1:
            return 1
            
        # Total moves = (moves to move n-1 to aux) + 1 + (moves to move n-1 to target)
        return 2 * self.towerOfHanoi(n - 1, fromm, aux, to) + 1

# or
class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        # 2^n - 1 using bitwise shift
        return (1 << n) - 1