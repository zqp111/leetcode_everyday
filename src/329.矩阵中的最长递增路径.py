#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        max_length = 0
        saved_re = [[-1]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_length = max(max_length, self.dfs(matrix, i, j, float('-inf'), saved_re))

        return max_length

    def dfs(self, matrix, i, j, last, saved_re):
        if i < 0 or j < 0 or i >=len(matrix) or j >= len(matrix[0]):
            return 0
        if matrix[i][j] <= last:
            return 0
        else:
            if saved_re[i][j] != -1:
                return saved_re[i][j]
            last = matrix[i][j]
            saved_re[i][j] = max([self.dfs(matrix, i+1, j, last, saved_re),
                        self.dfs(matrix, i-1, j, last, saved_re),
                        self.dfs(matrix, i, j+1, last, saved_re),
                        self.dfs(matrix, i, j-1, last, saved_re)]) + 1
            return saved_re[i][j]
# @lc code=end

