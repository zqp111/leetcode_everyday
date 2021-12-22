#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[-1][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(len(t)-1, -1, -1):
                if s[i] == t[j]:
                    dp[j][i] = dp[j+1][i+1] + dp[j][i+1]
                else:
                    dp[j][i] = dp[j][i+1]
        # print(dp)
        return dp[0][0]

# @lc code=end

