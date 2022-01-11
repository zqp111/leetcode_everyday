#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0: return False
        tmp = n
        while tmp:
            if tmp%2 ==1:
                return tmp == 1
            tmp = tmp >> 1
        
# @lc code=end

