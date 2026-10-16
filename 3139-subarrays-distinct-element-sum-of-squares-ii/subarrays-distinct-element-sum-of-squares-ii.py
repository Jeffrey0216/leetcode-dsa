class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        sq = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def update(node, start, end, left, right):
            if left <= start and end <= right:
                d = 1
                length = end - start + 1
                sq[node] = (
                    sq[node] + 2 * tree[node] + length
                ) % MOD
                tree[node] = (tree[node] + length) % MOD
                lazy[node] += d
                return
            mid = (start + end) // 2
            if lazy[node]:
                d = lazy[node]
                for child, l, r in (
                    (2 * node, start, mid),
                    (2 * node + 1, mid + 1, end)
                ):
                    length = r - l + 1
                    sq[child] = (
                        sq[child] + 2 * d * tree[child]
                        + length * d * d
                    ) % MOD
                    tree[child] = (
                        tree[child] + length * d
                    ) % MOD
                    lazy[child] += d

                lazy[node] = 0

            if left <= mid:
                update(2 * node, start, mid, left, right)

            if right > mid:
                update(2 * node + 1, mid + 1, end, left, right)

            tree[node] = (
                tree[2 * node] + tree[2 * node + 1]
            ) % MOD

            sq[node] = (
                sq[2 * node] + sq[2 * node + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans
