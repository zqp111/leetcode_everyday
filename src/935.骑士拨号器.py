#
# @lc app=leetcode.cn id=935 lang=python3
#
# [935] 骑士拨号器
#

# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        jump = [[4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]]
        dp = [[1]*10 for i in range(n)]
        for i in range(1, n):
            for j in range(10):
                tmp = 0
                for k in jump[j]:
                    tmp += dp[i-1][k]
                    tmp =int (tmp% (1e9+7))
                dp[i][j] = tmp
        return int (sum(dp[-1])% (1e9+7))
# @lc code=end

