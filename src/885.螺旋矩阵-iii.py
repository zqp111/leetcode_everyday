#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#

# @lc code=start
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        around = [(0, 1), (1, 0), (0, -1), (-1, 0)]  ##顺时针方向
        Left, Right, Upper, Bottom = cStart - 1, cStart + 1, rStart - 1, rStart + 1  ##四个方向的边界
        x, y, num, Dir = rStart, cStart, 1, 0  ##(x, y)为当前节点，num为当前查找的数字，Dir为当前的方向
        while num <= rows * cols:
            if x >= 0 and x < rows and y >= 0 and y < cols:  ##(x, y)在矩阵中
                res.append([x, y])
                num += 1
            if Dir == 0 and y == Right:  ##向右到右边界
                Dir += 1  ##调转方向向下
                Right += 1  ##右边界右移
            elif Dir == 1 and x == Bottom:  ##向下到底边界
                Dir += 1
                Bottom += 1  ##底边界下移
            elif Dir == 2 and y == Left:  ##向左到左边界
                Dir += 1
                Left -= 1  ##左边界左移
            elif Dir == 3 and x == Upper:  ##向上到上边界
                Dir = 0
                Upper -= 1  ##上边界上移
            x += around[Dir][0]
            y += around[Dir][1]
        return res

# @lc code=end

