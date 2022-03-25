#
# @lc app=leetcode.cn id=1267 lang=python3
#
# [1267] 统计参与通信的服务器
#

# @lc code=start
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0] * len(grid)
        col_count = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    ans += 1
        return ans
# @lc code=end

