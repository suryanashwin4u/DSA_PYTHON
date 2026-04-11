# Given two binary trees with their root nodes r1 and r2, return true if both of them are identical, otherwise return false.
# Note: Two trees are identical when they have the same data and the arrangement of the data is also same.

'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isIdentical(self, r1, r2):
        # If both nodes are null, trees are identical at this branch
        if not r1 and not r2:
            return True
        
        # If one is null and other is not, or data doesn't match
        if not r1 or not r2 or r1.data != r2.data:
            return False
            
        # Check left and right subtrees recursively
        return self.isIdentical(r1.left, r2.left) and self.isIdentical(r1.right, r2.right)