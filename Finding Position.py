# Some people(n) are standing in a queue. 
# A selection process follows a rule where people standing on even positions are selected. 
# Of the selected people a queue is formed and again out of these only people on even position are selected. 
# This continues until we are left with one person. 
# Find out the position of that person in the original queue.

# Expected Time Complexity: O(logn)
# Expected Auxiliary Space: O(1)

class Solution:
    def nthPosition(self, n):
        return 1 << (n.bit_length() - 1)

# or

class Solution:
    def nthPosition(self, n):
        ans = 1
        while ans * 2 <= n:
            ans *= 2
        return ans
