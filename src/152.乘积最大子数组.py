#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return [0,nums[0]][len(nums)]
        dp = max_dp = min_dp = nums[0]
        for i in range(1,len(nums)):
            max_dp, min_dp = max(max_dp * nums[i], nums[i], min_dp * nums[i]), min(max_dp * nums[i], nums[i], min_dp * nums[i])
            dp = max(dp, max_dp)
        return dp
# @lc code=end

