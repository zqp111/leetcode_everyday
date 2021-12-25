#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])):
                if i == len(matrix[0]) - 1:
                    dp[i][j] = matrix[i][j]
                else:
                    if j == 0:
                        dp[i][j] = matrix[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                    elif j == len(matrix[0]) - 1:
                        dp[i][j] = matrix[i][j] + min(dp[i+1][j], dp[i+1][j-1])
                    else:
                        dp[i][j] = matrix[i][j] + min([dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1]])
        return min(dp[0])
# @lc code=end

