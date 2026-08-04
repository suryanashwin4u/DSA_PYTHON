# Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 
# 0-based indexing is followed everywhere.
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

class Solution:
    def printGraph(self, V, edges):
        # Create adjacency list
        adj = [[] for _ in range(V)]
        
        # Add edges (undirected graph)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return adj