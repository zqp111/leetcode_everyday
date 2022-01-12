#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lenS1, lenS2 = len(s1), len(s2)
        if lenS1 + lenS2 != len(s3): return False
        dp = [[False]*(lenS1 + 1) for _ in range(lenS2 + 1)]
        dp[0][0] = True
        for i in range(1, lenS1+1):
            dp[0][i] = dp[0][i-1] and s1[i-1] == s3[i-1]
        for i in range(1, lenS2+1):
            dp[i][0] = dp[i-1][0] and s2[i-1] == s3[i-1]

        for i in range(1, lenS2+1):
            for j in range(1, lenS1+1):
                dp[i][j] = (dp[i-1][j] and s2[i-1] == s3[i + j-1]) or \
                            (dp[i][j-1] and s1[j-1] == s3[i + j-1])
        return dp[-1][-1]
# @lc code=end

