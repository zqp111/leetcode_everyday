#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = - int(str(-x)[::-1])
        else:    
            x = int(str(x)[::-1])
        if x < - (1<<31) or x > (1<<31):
            return 0
        return x
# @lc code=end

