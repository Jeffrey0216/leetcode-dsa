class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        for i in seq:
            if i == "(":
                depth += 1
                ans.append(depth%2)
            elif i == ")":
                ans.append(depth%2)
                depth -= 1
        return ans
        