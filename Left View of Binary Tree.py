# Given the root of a binary tree. Your task is to return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

# Note: If the tree is empty, return an empty list.

''' 
class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 
'''

from collections import deque

class Solution:
    def leftView(self, root):
        # If tree is empty
        if not root:
            return []
        
        ans = []
        q = deque([root])
        
        while q:
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                
                # First node of every level
                if i == 0:
                    ans.append(node.data)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        return ans