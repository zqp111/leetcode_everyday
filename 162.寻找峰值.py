#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int: 
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return l
# @lc code=end

