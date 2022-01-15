#
# @lc app=leetcode.cn id=1911 lang=python3
#
# [1911] 最大子序列交替和
#

# @lc code=start
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp= [nums[0], 0]
        for i in range(1, len(nums)):
            dp[0] = max(dp[0], dp[1]+nums[i])
            dp[1] = max(dp[1], dp[0]-nums[i]) 
        return max(dp)
# @lc code=end

