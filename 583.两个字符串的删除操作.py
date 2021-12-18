#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(m+1):
            dp[0][i] = i
        for i in range(n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j])
        # print(dp)
        return dp[-1][-1]
            
# @lc code=end

