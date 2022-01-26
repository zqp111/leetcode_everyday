#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not len(mat): return []

        m, n = len(mat), len(mat[0])
        c, r = 0, 0
        status = 0
        result = []
        while c < m and r < n:
            result.append(mat[c][r])
            if status == 0:
                c -= 1
                r += 1
                if c < 0 and r < n:
                    c = 0
                    status = 1
                elif r == n:
                    c += 2
                    r -= 1
                    status = 1
            else:
                c += 1
                r -= 1
                if r < 0 and c < m:
                    r = 0
                    status = 0
                elif c == m:
                    c -= 1
                    r += 2
                    status = 0
            # print(result)
        return result

# @lc code=end

