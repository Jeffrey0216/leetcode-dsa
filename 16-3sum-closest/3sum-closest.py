class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = float("inf")
        ans = 0
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low, high = i+1, n-1
            while low < high:
                summ = nums[i] + nums[low] + nums[high]
                if abs(summ - target) < abs(close - target):
                    close = summ
                if summ == target:
                    return summ
                elif summ < target:
                    low += 1
                else:
                    high -= 1
        return close
        