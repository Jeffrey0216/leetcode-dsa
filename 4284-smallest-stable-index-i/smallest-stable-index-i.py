class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            if max(nums[0:i+1]) - min(nums[i:n]) <= k:
                return i
        return -1
        