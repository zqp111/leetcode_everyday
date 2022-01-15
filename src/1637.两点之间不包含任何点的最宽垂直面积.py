#
# @lc app=leetcode.cn id=1637 lang=python3
#
# [1637] 两点之间不包含任何点的最宽垂直面积
#

# @lc code=start
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted([x for x, y in points])
        last= a[0]
        result = 0
        for i in range(1, len(a)):
            result = max(result, a[i]-last)
            last = a[i]
        return result

# @lc code=end

