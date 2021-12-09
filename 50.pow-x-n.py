#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        tmp = x
        ans = 1
        while n:
            if n&1:
                ans *= tmp
            tmp *= tmp
            # print(tmp)
            n = n >> 1
        print(ans)
        return ans
# @lc code=end

