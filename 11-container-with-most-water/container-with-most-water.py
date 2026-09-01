class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        a= -1
        while left < right:
            w = right - left
            h = min(height[left],height[right])
            area = w*h
            a = max(a,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return a
            
        