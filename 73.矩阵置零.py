#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_i, zero_j = [0]*len(matrix), [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])) :
                if not matrix[i][j]:
                    zero_i[i] =1
                    zero_j[j] =1
        for i in range(len(zero_i)):
            for j in range(len(zero_j)):
                if zero_i[i] or zero_j[j]:
                    matrix[i][j] = 0


# @lc code=end

