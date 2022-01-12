#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda k: [k[1], k[0]])
        result = 0
        last = intervals[0][1]
        for beg, end in intervals[1:]:
            if beg < last:
                result += 1
            else:
                last = end
        return result
        # print(intervals)
# @lc code=end

