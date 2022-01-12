#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        dp = [float('inf')] * len(s)
        self.isSame = [[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    self.isSame[i][j] = False
                elif j - i <= 1 or self.isSame[i+1][j-1]:
                    self.isSame[i][j] = True
                    
        # print(self.isSame)
        self.getMin(s, dp)
        # print(dp)
        return dp[len(s) - 1]

    
    def getMin(self, s, dp):
        if len(s) == 0:
            return 0
        if dp[len(s)-1] != float('inf'):
            return dp[len(s)-1]
        if self.isSame[0][len(s) - 1]:
            dp[len(s)-1] = 0
            return dp[len(s)-1]
        for i in range(len(s)-1, -1, -1):
            if self.isSame[len(s)-i-1][len(s) - 1]:
                dp[len(s)-1] = min(self.getMin(s[:len(s)-1-i], dp) + 1, dp[len(s)-1])
                if dp[len(s)-1] == 1:
                    break
        return dp[len(s)-1]
    
# @lc code=end

