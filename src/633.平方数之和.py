#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = sqrt(c)
        m = ceil(x)
        if x - m == 0:
            return True
        n = int(sqrt(c/2))
        # print(m, n)
        for i in range(n,m):
            q = sqrt(c-i**2)
            if q - int(q) == 0:
                return True
        return False
# @lc code=end

