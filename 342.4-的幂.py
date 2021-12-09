#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        if num ==1:
            return True
        n = bin(num)
        if len(n) < 5:
            return False
        if int(n[2]) != 1:
            return False
        if int(n[3:])!= 0:
            return False
        if len(n[3:])%2 !=0:
            return False
        return True
# @lc code=end

