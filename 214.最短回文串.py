#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        maxLen = 0
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j] and dp[i+1][j-1]: dp[i][j] = dp[i+1][j-1] + 2
                maxLen = max(maxLen, j-i+1)
        return maxLen 



# @lc code=end

