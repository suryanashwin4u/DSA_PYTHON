'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        # Base case
        if root is None:
            return
        
        # Step 1: Swap children
        root.left, root.right = root.right, root.left
        
        # Step 2: Recurse on left and right
        self.mirror(root.left)
        self.mirror(root.right)