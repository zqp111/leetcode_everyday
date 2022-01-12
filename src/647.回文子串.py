#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1 ,-1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j-i<= 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
            result += sum(dp[i])
        return result
# @lc code=end

