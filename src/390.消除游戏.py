#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] 消除游戏
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        def get_l(n):
            if n == 1:
                return 1
            return 2*get_r(n//2)
        def get_r(n):
            if n == 1:
                return 1
            return 2*get_l(n//2)-(n//2)*2+n-1
        return get_l(n)
        
# @lc code=end

