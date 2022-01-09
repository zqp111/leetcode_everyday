class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            numSum = nums[l] + nums[r]
            if numSum < target:
                l += 1
            elif numSum > target:
                r -= 1
            else: 
                return [nums[l], nums[r]]