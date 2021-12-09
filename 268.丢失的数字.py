#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ans ^= i
            ans ^= num
        ans ^= len(nums)
        return ans

# @lc code=end

