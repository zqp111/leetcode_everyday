#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ## 回溯法，超时
    #     self.result = 0
    #     self.backtracking(nums, 0, target)
    #     return self.result

    # def backtracking(self, nums, tmpsum, target):
    #     if len(nums) == 0:
    #         if tmpsum == target:
    #             self.result += 1
    #         return
    #     for symbol in [1, -1]:
    #         tmpsum += symbol*nums[0]
    #         self.backtracking(nums[1:], tmpsum, target)
    #         tmpsum -= symbol*nums[0]

        allSum = sum(nums)
        if abs(target) > allSum or (target+allSum)%2 == 1:
            return 0
        newTarget = (target + allSum)//2
        dp = [0]*(newTarget+1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(newTarget, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]
# @lc code=end

