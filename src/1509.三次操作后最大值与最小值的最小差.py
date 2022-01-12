#
# @lc app=leetcode.cn id=1509 lang=python3
#
# [1509] 三次操作后最大值与最小值的最小差
#

# @lc code=start
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0

        nums.sort()
        return min([nums[i-4]-nums[i] for i in range(4)])
# @lc code=end

