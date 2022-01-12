#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(0, len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                break
        else:
            return False
        
        nowLine = matrix[i]
        l, r = 0, len(nowLine)-1
        while l <= r: 
            mid = (l + r)//2
            if nowLine[mid] == target:
                return True
            elif nowLine[mid] < target:
                l = mid +1
            else:
                r = mid -1
        return False
# @lc code=end

