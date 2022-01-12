#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
            ## 多边形非凸个数
            ## 凸多边形的周长等于凸多边形外接（此外接仅限水平的矩形）矩形的周长。
            ## 凹多边形每一个凹的地方加2。
        # reversed = 0
        # li, lj, ri, rj = len(grid), len(grid[0]), 0, 0
        # u = 0
        # for i in range(len(grid)):
        #     reversed = 0
        #     for j in range(len(grid[0])):
        #         if grid[i][j]:
        #             lj = min(lj,j)
        #             rj = max(rj,j)
        #             if reversed ==0:
        #                 reversed =1
        #             elif reversed ==2:
        #                 reversed =1
        #                 u += 1
        #         else:
        #             if reversed ==1:
        #                 reversed =2
        
        # for j in range(len(grid[0])):
        #     reversed = 0
        #     for i in range(len(grid)):
        #         if grid[i][j]:
        #             li = min(li, i)
        #             ri = max(ri, i)
        #             if reversed ==0:
        #                 reversed =1
        #             elif reversed ==2:
        #                 reversed =1
        #                 u += 1
        #         else:
        #             if reversed ==1:
        #                 reversed =2
        # # print(ri, li, rj, lj, u)
        # return 2*(ri-li+1)+2*(rj-lj+1)+2*u


        ## dfs
        ## 核心点在于，当从陆地到达边缘或者水中时，边长加1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return self.dfs(grid, i, j)
    
    def dfs(self, grid, row, column):
        if row <0 or row >= len(grid) or column < 0 or column >= len(grid[0]): 
            return 1
        if grid[row][column] == 0:
            return 1
        if grid[row][column] == 2:
            return 0
        grid[row][column] = 2
        return self.dfs(grid, row, column + 1) + \
                self.dfs(grid, row, column - 1) + \
                self.dfs(grid, row + 1, column) + \
                self.dfs(grid, row - 1, column)
# @lc code=end

