#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')]*(len(cost)+1)
        dp[-1] = 0
        dp[-2] = 0
        for i in range(len(cost)-2, -1, -1):
            dp[i] = min(cost[i]+dp[i+1], cost[i+1]+dp[i+2])
        return dp[0]


# @lc code=end

