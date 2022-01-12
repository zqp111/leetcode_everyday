#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]*nums[1]
        b = nums[-2]*nums[-3]
        if nums[-1] < 0:
            return b*nums[-1]
        if a > b:
            return a*nums[-1]
        return b*nums[-1]
# @lc code=end

