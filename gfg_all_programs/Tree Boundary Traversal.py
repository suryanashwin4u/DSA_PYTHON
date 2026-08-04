# Given a root of a Binary Tree, return its boundary traversal in the following order:

# Left Boundary: Nodes from the root to the leftmost non-leaf node, preferring the left child over the right and excluding leaves.

# Leaf Nodes: All leaf nodes from left to right, covering every leaf in the tree.

# Reverse Right Boundary: Nodes from the root to the rightmost non-leaf node, preferring the right child over the left, excluding leaves, and added in reverse order.

# Note: The root is included once, leaves are added separately to avoid repetition, and the right boundary follows traversal preference not the path from the rightmost leaf.

# Time Complexity: O(n)
# Auxiliary Space: O(h)

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:

    def isLeaf(self, node):
        return node.left is None and node.right is None

    def addLeft(self, root, ans):
        curr = root.left

        while curr:
            if not self.isLeaf(curr):
                ans.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

    def addLeaves(self, root, ans):

        if root is None:
            return

        if self.isLeaf(root):
            ans.append(root.data)
            return

        self.addLeaves(root.left, ans)
        self.addLeaves(root.right, ans)

    def addRight(self, root, ans):

        curr = root.right
        temp = []

        while curr:

            if not self.isLeaf(curr):
                temp.append(curr.data)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        for i in range(len(temp)-1, -1, -1):
            ans.append(temp[i])

    def boundaryTraversal(self, root):

        if root is None:
            return []

        ans = []

        if not self.isLeaf(root):
            ans.append(root.data)

        self.addLeft(root, ans)

        self.addLeaves(root, ans)

        self.addRight(root, ans)

        return ans        
        