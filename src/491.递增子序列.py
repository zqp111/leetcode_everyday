#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [], result)
        return result

    def backtracking(self, nums, tmp, result):
        if len(tmp) >= 2:
            result.append(tmp.copy())
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            if i != 0:
                if nums[i] in nums[:i]:
                    continue
            if len(tmp) == 0:
                tmp.append(nums[i])
                self.backtracking(nums[i+1:], tmp, result)
                tmp.pop(-1)
            elif nums[i] >= tmp[-1]:
                tmp.append(nums[i])
                self.backtracking(nums[i+1:], tmp, result)
                tmp.pop(-1)
# @lc code=end

