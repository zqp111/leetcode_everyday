#
# @lc app=leetcode.cn id=1250 lang=python3
#
# [1250] 检查「好数组」
#
import math

# @lc code=start
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums) == 1: return nums[0] == 1
        uniGcd = math.gcd(nums[0], nums[1])
        if uniGcd == 1: return True
        for i in range(2, len(nums)):
            uniGcd = math.gcd(uniGcd, nums[i])
            if uniGcd == 1: return True
        return False
            
# @lc code=end

