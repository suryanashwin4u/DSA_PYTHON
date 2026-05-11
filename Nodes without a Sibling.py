# Given the root of a Binary Tree, find all nodes that do not have a sibling. Return the nodes in increasing order.

# Two nodes are considered siblings if they share the same parent.

# Note:

# The root node cannot have a parent, so it should not be included in the answer 
# If every node has a sibling, return a list containing only -1.

# Time Complexity: O(n log n)
# Auxiliary Space: O(n)

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def noSibling(self, root):
        ans = []

        def dfs(node):
            if not node:
                return

            # only left child
            if node.left and not node.right:
                ans.append(node.left.data)

            # only right child
            if node.right and not node.left:
                ans.append(node.right.data)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if not ans:
            return [-1]

        return sorted(ans)