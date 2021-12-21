#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, -prices[0]],[0, -prices[0]]]

        for i in range(len(prices)):
            dp[1][0] = max(dp[1][0], dp[1][1] + prices[i])
            dp[1][1] = max(dp[1][1], dp[0][0] - prices[i])
            dp[0][0] = max(dp[0][0], dp[0][1] + prices[i])
            dp[0][1] = max(dp[0][1],  - prices[i])
        return dp[1][0]
# @lc code=end

