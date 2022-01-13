#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
import heapq
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m1, m2, idx = -1, -1, 0
        for i, num in enumerate(nums):
            if num > m1:
                m1, m2, idx = num, m1, i
            elif num > m2:
                m2 = num
        return idx if m1 >= m2 * 2 else -1
# @lc code=end

