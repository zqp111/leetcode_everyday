#
# @lc app=leetcode.cn id=2017 lang=python3
#
# [2017] 网格游戏
#

# @lc code=start
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        up, down = sum(grid[0][1:]), 0
        result = max(up, down)
        for i in range(1, n):
            up -= grid[0][i]
            down += grid[1][i-1]
            result = min(result, max(up, down))
        return result

# @lc code=end

