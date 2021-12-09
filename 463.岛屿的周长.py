#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        reversed = 0
        li, lj, ri, rj = len(grid), len(grid[0]), 0, 0
        u = 0
        for i in range(len(grid)):
            reversed = 0
            for j in range(len(grid[0])):
                if grid[i][j]:
                    lj = min(lj,j)
                    rj = max(rj,j)
                    if reversed ==0:
                        reversed =1
                    elif reversed ==2:
                        reversed =1
                        u += 1
                else:
                    if reversed ==1:
                        reversed =2
        
        for j in range(len(grid[0])):
            reversed = 0
            for i in range(len(grid)):
                if grid[i][j]:
                    li = min(li, i)
                    ri = max(ri, i)
                    if reversed ==0:
                        reversed =1
                    elif reversed ==2:
                        reversed =1
                        u += 1
                else:
                    if reversed ==1:
                        reversed =2
        # print(ri, li, rj, lj, u)
        return 2*(ri-li+1)+2*(rj-lj+1)+2*u

# @lc code=end

