#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_ = min(nums)
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]-min_
        return ans
# @lc code=end

