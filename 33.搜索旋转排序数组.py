#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1] and target < nums[0]:
            return -1
        if target == nums[0]:
            return 0
        if target > nums[0] :
            l = 1
            while l < len(nums) and nums[l] <= target:
                if nums[l] < nums[l-1]:
                    return -1
                if nums[l] == target:
                    return l
                l += 1
            return -1
        if target == nums[-1]:
            return len(nums) -1 
        if target < nums[-1]:
            r = len(nums) -2
            while r >= 0 and nums[r] >= target:
                if nums[r] > nums[r + 1]:
                    return -1
                if target == nums[r]:
                    return r
                r -= 1
            return -1
# @lc code=end

