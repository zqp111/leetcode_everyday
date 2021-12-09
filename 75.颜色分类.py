#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums)-1
        idx = 0
        while idx <= r:
            if nums[idx] == 2:
                nums[idx], nums[r] = nums[r], nums[idx] 
                r -= 1
            elif nums[idx] == 1:
                idx +=1
            else:
                if idx == l:
                    l +=1
                    idx +=1
                else:
                    nums[idx], nums[l] = nums[l], nums[idx]  
                    l += 1

        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end

