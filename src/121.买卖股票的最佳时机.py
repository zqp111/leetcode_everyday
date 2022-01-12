#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <=1:
            return 0
    
        l1, g, l2 = prices[0], prices[0], prices[0]
        max_ = 0
        for i in prices[1:]:
            if i - l2 > max_:
                max_ = i - l2
                g = i
                l1 = l2
            elif i < l2:
                l2 = i
            elif i > g:
                if l1!=l2:
                    l1 = l2
                g = i
        return max_


# @lc code=end

