#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k:
            return 0
        dp = [[0, -prices[0]] for _ in range(k)]

        for i in range(len(prices)):
            for j in range(k-1, -1, -1):
                dp[j][0] = max(dp[j][0], dp[j][1]+ prices[i])
                if j > 0:
                    dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])
                else:
                    dp[j][1] = max(dp[j][1], - prices[i])
        return dp[k-1][0]
# @lc code=end

