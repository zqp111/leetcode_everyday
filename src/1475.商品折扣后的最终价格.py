#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = [0]*len(prices)

        stack = []
        for i in range(len(prices)):
            if not stack:
                stack.append(i)
            else:
                while stack and prices[stack[-1]] >= prices[i]:
                    cur_index = stack.pop(-1)
                    ans[cur_index] = prices[cur_index] - prices[i]
                stack.append(i)
        for i in range(len(stack)):
            ans[stack[i]] = prices[stack[i]]
        return ans
# @lc code=end

