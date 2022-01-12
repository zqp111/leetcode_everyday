#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1

        ## bfs 
        queue = [(0, 0)]
        grid[0][0] = 2
        target = (len(grid)-1, len(grid[0])-1)
        path = 0
        while queue:
            levelLen = len(queue)
            path += 1
            for _ in range(levelLen):
                cur = queue.pop(0)
                
                if cur == target: return path
                queue += self.addQueue(cur, grid)
        return -1


    def addQueue(self, cur, grid):
        nextPosition = []
        h, w = len(grid), len(grid[0])

        for i in range(max(0, cur[0] -1), min(h, cur[0]+2)):
            for j in range(max(0, cur[1] -1), min(w, cur[1]+2)):
                if not grid[i][j]:
                    nextPosition.append((i, j))
                    grid[i][j] = 2 
        return nextPosition


        
        
# @lc code=end

