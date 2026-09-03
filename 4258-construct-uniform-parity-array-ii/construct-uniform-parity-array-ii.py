class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallest = min(nums1)
        return smallest % 2 == 1 or all(i%2 == 0 for i in nums1)
