from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        arr = []

        for i, (start, end, weight) in enumerate(intervals):
            arr.append((end, start, weight, i))

        arr.sort()

        ends = [x[0] for x in arr]

        n = len(arr)

        dp = [[0] * 5 for _ in range(n + 1)]
        chosen = [[[] for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            end, start, weight, index = arr[i - 1]

            for j in range(1, 5):
                dp[i][j] = dp[i - 1][j]
                chosen[i][j] = chosen[i - 1][j][:]

                k = bisect_right(ends, start - 1)

                new_weight = dp[k][j - 1] + weight
                new_indices = chosen[k][j - 1] + [index]

                if new_weight > dp[i][j]:
                    dp[i][j] = new_weight
                    chosen[i][j] = new_indices
                elif new_weight == dp[i][j]:
                    if sorted(new_indices) < sorted(chosen[i][j]):
                        chosen[i][j] = new_indices

        return sorted(chosen[n][4])