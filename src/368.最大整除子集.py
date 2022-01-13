#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [1] * len(nums)
        resultLen = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j]+1)
                resultLen = max(resultLen, dp[i])
        result = []
        for i in range(len(nums)-1, -1, -1):
            if dp[i] == resultLen:
                if not result or result[0] % nums[i] == 0:
                    result.insert(0, nums[i])
                    resultLen -= 1
        return result
        
# @lc code=end

