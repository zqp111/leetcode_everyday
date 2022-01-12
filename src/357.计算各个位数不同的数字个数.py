#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0 :return 1
        if n > 10: n = 10
        result = 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 9
        for i in range(2, n+1):
            dp[i] = dp[i-1]*(11-i)
        return sum(dp)

# @lc code=end

