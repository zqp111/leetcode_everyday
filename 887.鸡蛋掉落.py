#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N == 1:
            return 1
        f = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, K + 1):
            f[1][i] = 1
        ans = -1
        for i in range(2, N + 1):
            for j in range(1, K + 1):
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
            if f[i][K] >= N:
                ans = i
                break
        return ans
# @lc code=end

