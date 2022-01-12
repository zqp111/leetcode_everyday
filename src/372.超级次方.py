#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        tmp = a%1337
        powa = 1
        for i in range(len(b)-1, -1, -1):
            powa *= pow(tmp, b[i])
            tmp = pow(tmp,10)%1337
        return powa %1337
        
# @lc code=end

