#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # result = 0
        # minNum = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] < minNum:
        #         result += i * (minNum - nums[i])
        #         minNum = nums[i]
        #     elif nums[i] > minNum:
        #         result += nums[i] - minNum
        # return result

        numSum = nums[0]
        minNum = nums[0]
        for i in range(1, len(nums)):
            numSum += nums[i]
            minNum = min(minNum, nums[i])
        return numSum-minNum*len(nums)

# @lc code=end

