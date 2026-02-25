from collections import deque
class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [0 for _ in range(n)]
        queue = deque()
        queue.append(0)
        visited[0] = 1
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for i in range(len(adj[node])):
                neigh = adj[node][i]
                if not visited[neigh]:
                    queue.append(neigh)
                    visited[neigh] = 1

        return ans

