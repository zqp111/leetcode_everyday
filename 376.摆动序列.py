#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]

        for i in range(len(nums)-2, -1, -1) :

            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1]+1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0]+1) 
                else:
                    dp[i][1] = max(dp[i][1], dp[j][1])
                    dp[i][0] = max(dp[i][0], dp[j][0])
        # print(dp)
        return max(dp[0])

# @lc code=end

