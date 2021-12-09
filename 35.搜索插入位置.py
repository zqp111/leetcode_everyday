#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = -1
        right = n
        while left != right:
            n = (left + right) // 2
            if nums[n] == target:
                return n
            elif nums[n] > target:
                right = n
            else:
                left = n
            if n == (left + right) // 2:
                return left +1
# @lc code=end

