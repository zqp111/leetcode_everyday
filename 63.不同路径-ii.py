#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 :
            return 0

        ans = [[0]*(len(obstacleGrid[0])+1) for i in range(len(obstacleGrid)+1)]
        
        # print(ans)
        for i in range(1, len(ans)):
            for j in range(1, len(ans[0])):
                if obstacleGrid[i-1][j-1] == 1:
                    ans[i][j] = 0
                elif i == 1 and j == 1:
                    ans[1][1] = 1
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        # print(ans)

        return ans[-1][-1]

# @lc code=end

