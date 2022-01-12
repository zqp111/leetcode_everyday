#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = len(nums)
        while l<r:
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
                r -= 1
            else:
                l += 1
            
        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

