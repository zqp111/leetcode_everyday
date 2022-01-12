#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        maxLen = 0
        result = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j] and j-i <= 1: dp[i][j] = j-i+1
                elif s[i]==s[j] and dp[i+1][j-1]: dp[i][j] = dp[i+1][j-1] +2
                if dp[i][j] > maxLen:
                    maxLen = dp[i][j]
                    result = s[i:j+1]

        return result
# @lc code=end

