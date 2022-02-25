#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        dp = [[float('inf')]*(len(weights)+1) for _ in range(days)]
        
        for i in range(days):
            dp[i][0] = 0

        for i in range(1, len(weights)+1):
            dp[0][i] = dp[0][i-1] + weights[i-1]

        for i in range(1, days):
            for j in range(i+1, len(weights)+1):
                for k in range(j, 0, -1):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k], sum(weights[k:j])))
        # print(dp)
        return dp[-1][-1]

# @lc code=end

