#
# @lc app=leetcode.cn id=757 lang=python3
#
# [757] 设置交集大小至少为2
#

# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals_ordered = sorted(intervals)
        print(intervals_ordered)
        left, right = intervals_ordered[0][1]-1, intervals_ordered[0][1]

        for i, j in intervals_ordered[1:]:
            left = max(left, i)
            right = min(right, j)
        print(left, right)
        return right - left + 3
# @lc code=end

