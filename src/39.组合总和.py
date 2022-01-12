#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        re, tmp = [], []
        self.backtracking(candidates, target, tmp, re)
        return re


    def backtracking(self, candidates, target, tmp, re):
        n = sum(tmp)
        if n == target:
            re.append(tmp.copy())
            return
        if n > target:
            return
        for i, num in enumerate(candidates) :
            tmp.append(num)
            self.backtracking(candidates[i:], target, tmp, re)
            tmp.pop()

# @lc code=end

