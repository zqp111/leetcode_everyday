#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        result = 0
        for i in range(len(matrix[0])) :
            dp[0][i] = int(matrix[0][i])
            result = max(result, dp[0][i])
        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            result = max(result, dp[i][0])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1
                else:
                    dp[i][j] = 0
                result = max(result, dp[i][j])
        return result**2
# @lc code=end

