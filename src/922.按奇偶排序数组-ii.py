#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        tmp = []
        i = 0
        while i < len(nums):
            if nums[i]%2:
                tmp.append(i)
            i += 2
        i = 1
        while i < len(nums):
            if nums[i]%2 == 0:
                j = tmp.pop(-1)
                nums[i], nums[j] = nums[j], nums[i]
            i += 2
        
        return nums
            
# @lc code=end

