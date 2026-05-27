# Given a binary tree, find its reverse level order traversal. 
# ie- the traversal must begin from the last level.

# Time Complexity: O(n)
# Auxiliary Space: O(n)

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

class Solution:
    def reverseLevelOrder(self, root):
        
        if not root:
            return []
        
        q = deque([root])
        st = []
        
        while q:
            node = q.popleft()
            
            st.append(node.data)
            
            # push right first
            if node.right:
                q.append(node.right)
                
            if node.left:
                q.append(node.left)
        
        return st[::-1]