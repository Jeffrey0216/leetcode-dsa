class Solution:
    def sortableIntegers(self,nums:list[int])->int:
        n=len(nums)
        pref_max=[0]*(n+1)
        suff_min=[float('inf')]*(n+1)
        drops=[0]*(n+1)
        for i in range(n):
            pref_max[i+1]=max(pref_max[i],nums[i])
            drops[i+1]=drops[i]
            if i>0 and nums[i-1]>nums[i]:
                drops[i+1]+=1
        for i in range(n-1,-1,-1):
            suff_min[i]=min(suff_min[i+1],nums[i])
        ans=0
        for k in range(1,n+1):
            if n%k!=0:
                continue
            valid=True
            for start in range(0,n,k):
                end=start+k-1
                count=drops[end+1]-drops[start+1]
                if nums[end]>nums[start]:
                    count+=1
                if count>1:
                    valid=False
                    break
                if start>0 and pref_max[start]>suff_min[start]:
                    valid=False
                    break
            if valid:
                ans+=k
        return ans