class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float("inf")
        window_sum = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                if (right - left + 1) < res:
                    res = (right - left + 1)
                window_sum -= nums[left]
                left += 1
        if res == float("inf"):
            return 0
        return res
            
                



        