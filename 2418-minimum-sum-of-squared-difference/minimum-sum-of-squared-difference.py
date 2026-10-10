class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a-b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            if sum(max(0, d-mid) for d in diff) <= k:
                right = mid
            else:
                left = mid + 1

        operations = sum(max(0, d-left) for d in diff)
        ans = sum(min(d, left) ** 2 for d in diff)
        extra = k - operations

        return ans - extra * (2 * left - 1)