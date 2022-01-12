#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        re =[]
        tmp = []
        self.backtrace([i for i in range(1, n+1, 1)], tmp, k, re)
        return re

    def backtrace(self, nums, tmp, k, re): 
        if len(tmp) == k:
            re.append(tmp.copy())
            return

        for i in range(len(nums)-k+len(tmp)+1):
            tmp.append(nums[i])
            self.backtrace(nums[i+1:], tmp, k, re)
            tmp.pop()
        #return list(itertools.combinations(range(1,n+1),k))
        
# @lc code=end

