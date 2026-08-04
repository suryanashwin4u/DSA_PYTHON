# Given a Binary Tree of size n, your task is to return the count of all the non-leaf nodes of the given binary tree.

class Solution:
    def countNonLeafNodes(self, root):
        # Base case: empty tree
        if root is None:
            return 0
        
        # If leaf node
        if root.left is None and root.right is None:
            return 0
        
        # Count this node + left subtree + right subtree
        return 1 + self.countNonLeafNodes(root.left) + self.countNonLeafNodes(root.right)