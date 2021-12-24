#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        dp = [[float('inf')]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]== s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][k]+dp[k+1][j], dp[i][j])
        # print(dp)
        return dp[0][-1]
# @lc code=end

