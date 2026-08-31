class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for char in t:
            need[char] = need.get(char,0) + 1
        window = {}
        left = 0
        have=0
        res = ""
        res_len = float("inf")
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1
            if c in need and need[c] == window[c]:
                have += 1
            while have == len(need):
                if (right - left + 1) < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1
                f = s[left]
                window[f] -= 1
                if f in need and window[f] < need[f]:
                    have -= 1
                left += 1
        return res



        