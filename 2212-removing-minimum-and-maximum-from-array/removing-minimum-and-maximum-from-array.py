class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        a = nums.index(min(nums))
        b = nums.index(max(nums))

        left = max(a, b) + 1
        right = n - min(a, b)

        one_each = min(a, b) + 1 + n - max(a, b)

        return min(left, right, one_each)