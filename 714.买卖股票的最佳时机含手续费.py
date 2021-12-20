#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # all_up = []
        # stack = []
        # for i in range(len(prices)):
        #     if len(stack) == 0:
        #         stack.append(prices[i])
        #     elif len(stack) == 1:
        #         if prices[i] - stack[-1] > fee:
        #             stack.append(prices[i])
        #         elif prices[i] < stack[-1]:
        #             stack[-1] = prices[i]
        #     elif len(stack) == 2:
        #         if prices[i] > stack[-1]:
        #             stack[-1] = prices[i]
        #         else:
        #             all_up.append(stack.copy())
        #             stack = [prices[i]]
        # if len(stack) == 2:
        #     all_up.append(stack.copy())
        
        # if len(all_up) == 0:
        #     return 0

        # if len(all_up)==1:
        #     return all_up[0][1] - all_up[0][0] - fee

        # l, r = all_up[0]
        # result = 0

        # for i in range(1, len(all_up)):
        #     if r -fee < all_up[i][0]:
        #         r = all_up[i][1]
        #     else:
        #         result += r-l-fee
        #         l, r = all_up[i]
        # result += r-l-fee

        # return result

        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit

                    

# @lc code=end

