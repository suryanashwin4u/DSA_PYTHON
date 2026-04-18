# Given the root of a binary Tree. 
# Your task is to return the right view of the binary tree. 
# The right view of a Binary Tree is the set of nodes visible when the tree is viewed from the right side.

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
# Level Order Traversal (BFS) — Recommended
class Solution:
    def rightView(self, root):
        if not root:
            return []
        
        from collections import deque
        q = deque([root])
        ans = []
        
        while q:
            size = len(q)
            
            for i in range(size):
                node = q.popleft()
                
                # last node of level
                if i == size - 1:
                    ans.append(node.data)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans
    
# DFS (Right-first traversal)
class Solution:
    def rightView(self, root):
        ans = []
        
        def dfs(node, level):
            if not node:
                return
            
            if level == len(ans):
                ans.append(node.data)
            
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return ans