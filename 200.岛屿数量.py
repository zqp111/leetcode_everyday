#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res
    

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >=len(grid) or j >= len(grid[0]):
            return 
        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)
# @lc code=end

