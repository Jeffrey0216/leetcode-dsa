
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        n = len(nums)

        # Sort by digit sum, then by number
        arr = sorted(
            [(digit_sum(x), x, i) for i, x in enumerate(nums)]
        )

        # Map each original index to its target index
        pos = [0] * n
        for target, (_, _, original) in enumerate(arr):
            pos[original] = target

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[j]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps
