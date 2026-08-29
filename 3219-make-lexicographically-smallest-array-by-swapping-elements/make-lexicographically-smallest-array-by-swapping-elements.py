class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = nums[:]

        i = 0

        while i < len(nums):
            j = i

            while j + 1 < len(nums) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j + 1))
            values = [arr[k][0] for k in range(i, j + 1)]

            for k in range(len(indices)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans