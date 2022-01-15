#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0
        mx = values[0]
        for i in range(1, len(values)):
            result = max(result, mx+values[i] - i)
            mx = max(mx, values[i]+i)
        return result
# @lc code=end

