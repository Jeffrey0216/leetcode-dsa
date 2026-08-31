class Solution:
    def lengthOfLongestSubstring(self, s):
        sett = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            res = max(res,right - left + 1)
        return res

