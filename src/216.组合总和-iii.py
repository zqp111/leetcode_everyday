#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        re =[]
        tmp = []
        self.backtrace([i for i in range(1, 10, 1)], tmp, k, re, n)
        return re

    def backtrace(self, nums, tmp, k, re, n): 
        
        if len(tmp) == k:
            summ = sum(tmp)
            if summ == n:
                re.append(tmp.copy())
            return

        # if summ >= n:
        #    return

        for i in range(len(nums)-k+len(tmp)+1):
            tmp.append(nums[i])
            self.backtrace(nums[i+1:], tmp, k, re, n)
            tmp.pop()
# @lc code=end

