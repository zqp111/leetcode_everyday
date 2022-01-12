#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        re = [-1]*len(nums)
        def get_max(split_nums, re):
            if len(split_nums) == 0:
                return 0
            if len(split_nums) == 1:
                re[0] = split_nums[0]
                return re[0]
            if re[len(split_nums) - 1] >=0:
                return re[len(split_nums)-1]
            re[len(split_nums)-1] = max(split_nums[0]+get_max(split_nums[2:], re), 
                                        split_nums[1]+get_max(split_nums[3:], re))
            return re[len(split_nums)-1]
        get_max(nums, re)
        return re[-1]

# @lc code=end

