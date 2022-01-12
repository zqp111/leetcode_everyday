#
# @lc app=leetcode.cn id=576 lang=python3
#
# [576] 出界的路径数
#

# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        import numpy as np

        if maxMove == 0:
            return 0

        ans = np.zeros((maxMove, m, n), dtype=np.uint32)
        ans[0, startRow, startColumn] = 1

        def fresh_ans(mat_pre):
            
            newMat = np.zeros((m+2, n+2), dtype=np.uint32)
            newMat[1:-1, 1:-1] = mat_pre

            return newMat[2:, 1:-1] + newMat[0:-2, 1:-1] + \
                  newMat[1:-1, 2:] + newMat[1:-1, 0:-2]  


        for i in range(1, maxMove):
            ans[i] = fresh_ans(ans[i-1])%(1e9+7)

        return int(ans[:, 0, :].sum() + ans[:, -1, :].sum() + \
                ans[:, :, 0].sum() + ans[:, :, -1].sum())%(1e9+7)

# @lc code=end

