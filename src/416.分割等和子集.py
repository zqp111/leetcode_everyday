#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        allNumSum = sum(nums)
        if allNumSum % 2 != 0: return False
        targetNum = allNumSum // 2

        dp = [float('-inf')]*(targetNum+1)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(targetNum, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]]+1)
        return dp[targetNum] != float('-inf')
# @lc code=end

