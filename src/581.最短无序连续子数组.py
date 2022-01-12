#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] < stack[-1]:
                while nums[i] < stack[-1]:
                    stack.pop(-1)
                

# @lc code=end

