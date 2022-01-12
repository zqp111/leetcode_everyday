#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, -prices[0]
        lastBuy = 0
        for i in range(len(prices)):
            # print(buy, sell)
            tmp = buy
            buy = max(buy, sell+prices[i])
            sell = max(sell, lastBuy-prices[i])
            lastBuy = tmp
        return buy
# @lc code=end

