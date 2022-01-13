#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:

        dp = [0, 1, 1]
        if n <= 2: return dp[n]
        for _ in range(n-2):
            tmp = sum(dp)
            dp = dp[1:]+[tmp]
        return tmp
# @lc code=end

