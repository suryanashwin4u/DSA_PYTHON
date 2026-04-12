# Given the root of a binary tree. Check whether it is a BST or not.

# A BST is defined as follows:

# The left subtree of a node contains only nodes with data less than the node's data.
# The right subtree of a node contains only nodes with data greater than the node's data.
# Both the left and right subtrees must also be binary search trees.
# Note: We are considering that BSTs can not contain duplicate Nodes.

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isBST(self, root):
        def helper(node, low, high):
            if not node:
                return True
            
            if not (low < node.data < high):
                return False
            
            return (helper(node.left, low, node.data) and
                    helper(node.right, node.data, high))
        
        return helper(root, float('-inf'), float('inf'))