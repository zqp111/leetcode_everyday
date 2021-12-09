#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        s = [1 if i <=2 else 0 for i in range(n+1)]
        def find_max_n(n, s):
            if s[n]>0:
                return s[n]
            else:
                max_ = 0
                for k in range(1, n):
                    q = max(k*find_max_n(n-k, s), k*(n-k))
                    if q > max_:
                        max_ = q
                s[n] = max_
                return max_
        find_max_n(n, s)
        return s[n]
# @lc code=end

