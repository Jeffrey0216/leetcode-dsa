class Solution:
    def maxPalindromes(self,s,k):
        n=len(s)
        p=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<2 or p[i+1][j-1]):
                    p[i][j]=True
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i-1]
            for j in range(i-k+1):
                if i-j>=k and p[j][i-1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return dp[n]
        