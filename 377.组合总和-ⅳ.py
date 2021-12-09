#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        re = [-1 for _ in range(len(target)+1)]
        def get_n(nums, target):
            if re[target] >= 0:
                return nums[target]
            for 

# @lc code=end

