class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1]*n
        for i in range(2, n):
            for j in range(i-1, -1, -1):
                dp[i] = max(dp[i], (i-j)*dp[j], (i-j)*(j+1))
        # print(dp)
        return dp[-1]