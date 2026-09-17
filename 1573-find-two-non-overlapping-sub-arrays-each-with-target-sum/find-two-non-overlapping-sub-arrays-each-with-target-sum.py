class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        ans = float('inf')
        s = 0
        last = {}

        for i, x in enumerate(arr):
            s += x
            if s == target:
                length = i + 1
                if i > 0 and dp[i - 1] != float('inf'):
                    ans = min(ans, length + dp[i - 1])
                dp[i] = length

            if s - target in last:
                j = last[s - target]
                length = i - j
                if j >= 0 and dp[j] != float('inf'):
                    ans = min(ans, length + dp[j])

                dp[i] = min(dp[i], length)

            if i > 0:
                dp[i] = min(dp[i], dp[i - 1])

            last[s] = i

        return -1 if ans == float('inf') else ans