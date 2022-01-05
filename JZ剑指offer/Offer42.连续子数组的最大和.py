class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        result = dp
        for num in nums[1:]:
            dp = max(dp+num, num)
            result = max(result, dp)
        return result
