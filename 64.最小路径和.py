#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        for i in range(len(grid)-2, -1, -1):
            dp[i][-1] = grid[i][-1] + dp[i+1][-1]
        for i in range(len(grid[0])-2, -1, -1):
            dp[-1][i] = grid[-1][i] + dp[-1][i+1]
        
        for i in range(len(grid)-2, -1, -1):
            for j in range(len(grid[0])-2, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]
        # print(dp)
        return dp[0][0]

# @lc code=end

