#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        for end in range(len(s)):
            for start in range(end, -1, -1):
                if start == end:
                    dp[start][end] = 1
                elif s[start] == s[end]:
                    dp[start][end] = dp[start+1][end-1] + 2
                else:
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
        return dp[0][-1]

# @lc code=end

