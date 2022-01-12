#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.result = 0
        self.backtracking([], n)
        return self.result
    
    def _can_site(self, tmp, index):
        if index in tmp:
            return False
        j = len(tmp)
        for i, used in enumerate(tmp):
            if j - i == index - used or j - i == used - index:
                return False
        return True

    def backtracking(self, tmp, n):
        if len(tmp) == n:
            self.result += 1
            return
        
        for i in range(n):
            if self._can_site(tmp, i):
                tmp.append(i)
                self.backtracking(tmp, n)
                tmp.pop(-1)
# @lc code=end

