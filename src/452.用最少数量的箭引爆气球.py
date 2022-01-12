#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort()
        # print(points)
        nums = 1
        # left = points[0][0]
        right = points[0][1]
        for l in points[1:]:
            if l[0] <= right:
                # left =l[0]
                right = min(l[1], right)
            elif l[0] > right:
                nums += 1
                # left = l[0]
                right = l[1]
        # print(nums)
        return nums

# @lc code=end

