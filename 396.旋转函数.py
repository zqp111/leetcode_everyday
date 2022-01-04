#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = sum([i*nums[i] for i in range(len(nums))])
        numSum = sum(nums)
        n = len(nums)
        result = dp[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + numSum - n*nums[n-i]
            result = max(result, dp[i])
        return result
# @lc code=end

