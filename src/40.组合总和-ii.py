#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        re, tmp = [], []
        candidates.sort()
        # print(candidates)
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
            if i !=0 and num == candidates[i-1]:
                continue
            tmp.append(num)
            self.backtracking(candidates[i+1:], target, tmp, re)
            tmp.pop()

# @lc code=end

