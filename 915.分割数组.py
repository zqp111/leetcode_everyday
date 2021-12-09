#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left = 1
        left_max = A[0]
        left_max_current = A[0]
        for i, x in enumerate(A):
            if x >= left_max:
                left_max_current = max(left_max_current, x)
            elif x < left_max:
                left = i+1
                left_max = left_max_current
        return left
# @lc code=end

