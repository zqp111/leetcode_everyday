#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## dp
        # if not nums:
        #     return 0
        # dp = []
        # for i in range(len(nums)):
        #     dp.append(1)
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)            


        ## greedy search
        
        if not nums: return 0
        minEnd = [nums[0]]
        maxLen = 1
        for i in range(1, len(nums)):
            index = bisect_left(minEnd, nums[i])
            if index == len(minEnd):
                minEnd.append(nums[i])
                maxLen += 1
            else:
                minEnd[index] = nums[i]
        return maxLen
            

# @lc code=end

