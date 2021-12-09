#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n :
            a = n & 1
            b = (n & 2) >>1
            # print(a, b)
            if a == b:
                return False
            n >>= 1
        return True
# @lc code=end

