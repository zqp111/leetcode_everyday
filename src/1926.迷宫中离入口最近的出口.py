#
# @lc app=leetcode.cn id=1926 lang=python3
#
# [1926] 迷宫中离入口最近的出口
#

# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r,c = len(maze), len(maze[0])
        
        queue = [entrance]
        pathLen = 0
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            level = len(queue)
            for _ in range(level):
                cur = queue.pop(0)
                nextPosition = self.getNext(maze, cur)
                for position in nextPosition:
                    queue.append(position)
                    if position[0] == 0 or position[0] == r-1 or position[1] == 0 or position[1] == c-1:
                        return pathLen + 1
                    maze[position[0]][position[1]] = '+'
            pathLen += 1
        return -1
        
    def getNext(self, maze, cur):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        r,c = len(maze), len(maze[0])
        nextPosition = []
        for move in moves:
            newPosition = [cur[0] + move[0], cur[1] + move[1]]
            if 0<=newPosition[0]<r and 0<=newPosition[1]<c:
                if maze[newPosition[0]][newPosition[1]] == '.':
                    nextPosition.append(newPosition.copy())
        return nextPosition

# @lc code=end

