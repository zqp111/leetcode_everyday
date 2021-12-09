#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0 for _ in range(n+1)]
        def get_n(n, res):
            if res[n] >0:
                return res[n]
            if n <=2:
                res[n] = n
                return res[n]
            else:
                res[n] = get_n(n-1, res) + get_n(n-2, res)
                return res[n]
        get_n(n, res)
        return res[n]
# @lc code=end

