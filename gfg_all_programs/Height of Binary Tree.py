# Given the root of a binary tree, your task is to find the maximum depth of the tree.
# Note: The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

class Solution:
    def height(self, root):
        # Base case
        if root is None:
            return -1
        
        # Recursive case
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # Return max height + 1 edge
        return max(left_height, right_height) + 1

