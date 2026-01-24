class Solution:

    def findPath(self, i, j, visited, move, ans, n, maze):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        visited[i][j] = 1
        # downward
        if i + 1 < n and not visited[i + 1][j] and maze[i + 1][j] == 1:
            self.findPath(i + 1, j, visited, move + "D", ans, n, maze)
        # left

        if j - 1 >= 0 and not visited[i][j - 1] and maze[i][j - 1] == 1:
            self.findPath(i, j - 1, visited, move + "L", ans, n, maze)
        # right
        if j + 1 < n and not visited[i][j + 1] and maze[i][j + 1] == 1:
            self.findPath(i, j + 1, visited, move + "R", ans, n, maze)

        # upward
        if i - 1 >= 0 and not visited[i - 1][j] and maze[i - 1][j] == 1:
            self.findPath(i - 1, j, visited, move + "U", ans, n, maze)

        visited[i][j] = 0

    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        ans = []
        if maze[0][0] == 0:
            return ans

        visited = [[0] * n for _ in range(n)]
        self.findPath(0, 0, visited, "", ans, n, maze)
        return ans