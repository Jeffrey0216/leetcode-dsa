class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            total = grid[i][j]
            grid[i][j] = 0

            while stack:
                x, y = stack.pop()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    a, b = x + dx, y + dy

                    if 0 <= a < m and 0 <= b < n and grid[a][b] > 0:
                        total += grid[a][b]
                        grid[a][b] = 0
                        stack.append((a, b))

            return total

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if dfs(i, j) % k == 0:
                        count += 1

        return count