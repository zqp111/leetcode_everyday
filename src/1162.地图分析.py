#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        queue = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1: 
                    queue.append([i, j])
        if len(queue) == 0 or len(queue) == r*c:
            return -1
        
        path = 0

        while queue:
            # print(queue)
            level = len(queue)
            for _ in range(level):
                cur = queue.pop(0)
                nextPosition = self.getNext(grid, cur)
                for position in nextPosition:
                    grid[position[0]][position[1]] = 1
                    queue.append(position)
            path += 1
        return path -1

    def getNext(self, grid, cur):
        r, c = len(grid), len(grid[0])
        nextPosition = []
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for move in moves:
            newPosition = [cur[0]+move[0], cur[1]+move[1]]
            if 0<=newPosition[0]<r and 0<= newPosition[1] < c:
                if grid[newPosition[0]][newPosition[1]] == 0: 
                    nextPosition.append(newPosition.copy())
        return nextPosition

# @lc code=end

