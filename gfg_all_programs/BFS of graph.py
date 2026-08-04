# Given a connected undirected graph containing V vertices, 
# represented by a 2-d adjacency list adj[][], 
# where each adj[i] represents the list of vertices connected to vertex i. 
# Perform a Breadth First Search (BFS) traversal starting from vertex 0, 
# visiting vertices from left to right according to the given adjacency list, 
# and return a list containing the BFS traversal of the graph.

# Note: Do traverse in the same order as they are in the given adjacency list.

# Time Complexity: O(V + E)
# Auxiliary Space: O(V + E)

from collections import deque

class Solution:
    def bfs(self, adj):

        n = len(adj)

        visited = [False] * n
        q = deque()
        ans = []

        q.append(0)
        visited[0] = True

        while q:

            node = q.popleft()
            ans.append(node)

            for nei in adj[node]:

                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return ans