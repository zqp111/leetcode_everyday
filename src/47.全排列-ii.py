#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtracking(nums, [], result)
        return result
    
    def backtracking(self, nums, tmp, re):
        if len(nums) == 0:
            re.append(tmp.copy())
            return
        for i in range(len(nums)):
            if nums[i] not in nums[:i]:
                tmp.append(nums[i])
                self.backtracking(nums[:i]+nums[i+1:], tmp, re)
                tmp.pop(-1)
        
# @lc code=end

