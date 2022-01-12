#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        import numpy as np

        a, b = len(word1), len(word2)
        if not a*b:
            return max(a, b)

        res = np.zeros((a+1, b+1), dtype=np.int64)

        res[0, 1:] = np.arange(1, res.shape[1])
        res[1:, 0] = np.arange(1, res.shape[0])

        for i in range(1, res.shape[0]):
            for j in range(1, res.shape[1]):
                if word1[i-1] != word2[j-1]:
                    m = 1
                else:
                    m = 0
                res[i, j] = min(res[i-1, j]+1, res[i, j-1]+1, res[i-1, j-1]+m)
        print(res[-1, -1])
        return int(res[-1, -1])

# @lc code=end

