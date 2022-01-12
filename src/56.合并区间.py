#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        begin = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                ans.append([begin, end])
                begin,end = interval[0], interval[1]
        ans.append([begin, end])
        return ans
# @lc code=end

