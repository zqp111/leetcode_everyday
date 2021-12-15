#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        max_dp = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0]+1 > dp[i][0]:
                        dp[i][0] = dp[j][0]+1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0]+1 == dp[i][0]:
                        dp[i][1] += dp[j][1]

                    max_dp = max(dp[i][0], max_dp)
        re = 0
        # print(dp)
        for i in range(len(dp)):
            if dp[i][0] == max_dp:
                re += dp[i][1]
        return re


# @lc code=end

