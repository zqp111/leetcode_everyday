#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        result, tmp = 0, 0
        sub = nums[0] - nums[1]
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i] == sub:
                tmp += 1
            else:
                sub = nums[i-1] - nums[i]
                tmp = 0
            result += tmp
        return result
# @lc code=end

