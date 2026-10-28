class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        length = 0
        for c in s:
            count[c] = count.get(c,0) + 1
            if count[c] % 2 == 0:
                length += 2
        if length < len(s):
            length += 1
        return length