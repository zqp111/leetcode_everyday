#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] 乘积为正数的最长子数组长度
#

# @lc code=start
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        if nums[0] > 0:
            dp = [1, 0]
        elif nums[0] < 0:
            dp = [0, 1]
        else:
            dp = [0, 0]
        result = dp[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[0] = dp[0] + 1
                dp[1] = dp[1] + 1 if dp[1] else 0
            elif nums[i] < 0:
                old = dp[0]
                dp[0] = dp[1] + 1 if dp[1] else 0
                dp[1] = old + 1
            else:
                dp[0] = dp[1] = 0
            result = max(result, dp[0])
            # print(dp, result)
        return result
                
# @lc code=end

