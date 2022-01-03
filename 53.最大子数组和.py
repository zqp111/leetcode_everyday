#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sumArray = [0]
        # tmpSum = 0
        
        # for num in nums:
        #     tmpSum += num

        #     sumArray.append(tmpSum)
        # mintmp = sumArray[0]
        # result = float('-inf')
        # for num in sumArray[1:]:
        #     result = max(result, num-mintmp)
        #     mintmp = min(mintmp, num)
        # return result
        mintmp = 0
        tmpSum = 0
        result = float('-inf')
        for num in nums:
            tmpSum += num
            result = max(result, tmpSum-mintmp)
            mintmp = min(mintmp, tmpSum)
        return result
        
        
# @lc code=end

