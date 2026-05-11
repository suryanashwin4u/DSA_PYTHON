# Given a binary tree and an integer target, 
# check whether there is a root-to-leaf path with its sum as target.
# Time Complexity: O(n)
# Auxiliary Space: O(Height of Binary Tree)

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        
        if not root:
            return False

        target -= root.data

        # leaf node
        if not root.left and not root.right:
            return target == 0

        return (self.hasPathSum(root.left, target) or
                self.hasPathSum(root.right, target))