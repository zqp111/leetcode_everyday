#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.backtracking(nums, [], result)
        return result


    def backtracking(self, nums, tmp, result):
        result.append(tmp.copy())
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                tmp.append(nums[i])
                self.backtracking(nums[i+1:], tmp, result)
                tmp.pop(-1)
# @lc code=end

