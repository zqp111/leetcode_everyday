#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp = [[False]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            dp[i][i] = matrix[i][i] == 1
            for j in range(i, len(matrix[0])):
# @lc code=end

