# Given the root of a binary search tree and a number k, 
# find the greatest number in the binary search tree that is less than or equal to k.

# Note: If no such node value exists that is smaller than k, then return -1.

# Time Complexity: O(h)
# Auxiliary Space: O(h)

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        ans = -1

        while root:

            if root.data == k:
                return k

            if root.data < k:
                ans = root.data
                root = root.right
            else:
                root = root.left

        return ans
