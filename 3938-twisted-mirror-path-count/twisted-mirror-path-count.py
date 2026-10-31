class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Starting from (0, 0)
        dp[0][1][0] = 1
        dp[1][0][1] = 1

        for i in range(m):
            for j in range(n):

                if (i, j) == (0, 0):
                    continue

                right = dp[i][j][0]
                down = dp[i][j][1]

                if grid[i][j] == 1:

                    # Entered mirror while moving right
                    if right and i + 1 < m:
                        dp[i + 1][j][1] += right
                        dp[i + 1][j][1] %= MOD

                    # Entered mirror while moving down
                    if down and j + 1 < n:
                        dp[i][j + 1][0] += down
                        dp[i][j + 1][0] %= MOD

                else:

                    # Move right
                    if j + 1 < n:
                        dp[i][j + 1][0] += right + down
                        dp[i][j + 1][0] %= MOD

                    # Move down
                    if i + 1 < m:
                        dp[i + 1][j][1] += right + down
                        dp[i + 1][j][1] %= MOD

        return sum(dp[m - 1][n - 1]) % MOD