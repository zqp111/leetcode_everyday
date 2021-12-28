# @algorithm @lc id=100275 lang=python3 
# @title shu-zu-zhong-zhong-fu-de-shu-zi-lcof


from cn.Python3.mod.preImport import *
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])
