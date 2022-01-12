#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0

        for i in range(n-2, -1, -1):
            for j in range(min(nums[i], n-1-i)):
                dp[i] = min(dp[i], dp[i+j+1]+1)
        # print(dp)
        return dp[0]
# @lc code=end

