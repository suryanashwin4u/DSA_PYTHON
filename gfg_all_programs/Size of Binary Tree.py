# Given a binary tree, you have to return the size of it. 
# Size of binary tree is defined as number of nodes in it.

from typing import Optional
from collections import deque
"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def getSize(self, node):
    
        # Base case: if tree is empty
        if node is None:
            return 0
        
        # Count current node + left subtree + right subtree
        return 1 + self.getSize(node.left) + self.getSize(node.right)
