#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        re = []
        self.backtracking(nums, [], re)
        return re
    
    def backtracking(self, nums, tmp, re):
        if not nums:
            re.append(tmp.copy())
        for i in range(len(nums)):
            tmp.append(nums[i])
            self.backtracking(nums[:i]+nums[i+1:], tmp, re)
            tmp.pop(-1)

# @lc code=end

