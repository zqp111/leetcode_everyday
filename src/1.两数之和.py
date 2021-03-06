#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            if seen.get(nums[i], None) is None:
                seen[target-nums[i]] = i
            else:
                return [seen[nums[i]], i]
# @lc code=end

