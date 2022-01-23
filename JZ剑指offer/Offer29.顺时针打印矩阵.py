#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def one(x1, y1, x2, y2, ans, M):
            i, j = x1, y1
            for j in range(y1, y2):
                ans.append(M[i][j])
            if i+1 == x2:
                return
            for i in range(x1+1, x2):
                ans.append(M[i][j])
            if j == y1:
                return
            for j in range(y2-2, y1-1, -1):
                ans.append(M[i][j])
            for i in range(x2-2, x1, -1):
                ans.append(M[i][j])
        if len(matrix) == 0:
            return []
        x1, x2 = 0, len(matrix)
        y1, y2 = 0, len(matrix[0])
        ans = []
        while x1+1 <= x2 and y1+1 <= y2:
            one(x1, y1, x2, y2, ans, matrix)
            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1
        # print(ans)
        return ans
# @lc code=end

