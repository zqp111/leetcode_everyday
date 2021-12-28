#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#

# @lc code=start
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        for i in range(0, len(nums)):
            min_val, max_val = nums[i], nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] < min_val:
                    min_val = nums[j]
                elif nums[j] > max_val:
                    max_val = nums[j]
                result += max_val - min_val
        return result
# @lc code=end
