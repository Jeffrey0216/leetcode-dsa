class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        need = {}
        for i in s1:
            need[i] = need.get(i,0) + 1
        window =  {}
        for right in range(len(s2)):
            a = s2[right]
            window[a] = window.get(a,0 ) + 1
            while (right - left +1) > len(s1):
                window[s2[left]] -= 1 
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if need == window:
                return True
        return False


        
            