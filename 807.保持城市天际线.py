#
# @lc app=leetcode.cn id=807 lang=python3
#
# [807] 保持城市天际线
#

# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        l, up = [], []
        for i in range(len(grid)):
            l.append(max(grid[i]))
        for j in range(len(grid[i])):
            # print(grid[:][j])
            up.append(max(grid[i][j]for i in range(len(grid)) ))
        result = 0
        # print(l, up)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print(min(l[i], up[j]))
                result += min(l[i], up[j])-grid[i][j]
        return result
# @lc code=end

