#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1= points[0][0]-points[1][0], points[0][1]-points[1][1]
        x2, y2= points[0][0]-points[2][0], points[0][1]-points[2][1]
        if x2 == 0 or y2 == 0:
            if x2 == y2:
                return False
            elif x1 == 0 and x2 == 0:
                return False
            elif y1 == 0 and y2 == 0:
                return False
            return True
        return not x1/x2==y1/y2
# @lc code=end

