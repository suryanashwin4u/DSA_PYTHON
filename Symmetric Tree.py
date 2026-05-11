# Given the root of a binary tree, check whether it is symmetric, i.e., whether the tree is a mirror image of itself.
# Note: A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.
# Time Complexity: O(n)
# Auxiliary Space: O(h)

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isSymmetric(self, root):

        def mirror(left, right):

            # both null
            if not left and not right:
                return True

            # one null
            if not left or not right:
                return False

            # values different
            if left.data != right.data:
                return False

            # check mirror structure
            return (mirror(left.left, right.right) and
                    mirror(left.right, right.left))

        if not root:
            return True

        return mirror(root.left, root.right)