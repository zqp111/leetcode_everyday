#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#

# @lc code=start
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        for i in range(1, len(grid)): 
            for j in range(len(grid[0])):
                if grid[i-1][j]:
                    grid[i][j] = grid[i-1][j] + 1
                else:
                    grid[i][j] = grid[i][j-1] + 1
# @lc code=end

