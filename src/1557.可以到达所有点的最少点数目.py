#
# @lc app=leetcode.cn id=1557 lang=python3
#
# [1557] 可以到达所有点的最少点数目
#

# @lc code=start


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inAngle = [0]*n
        for edge in edges:
            inAngle[edge[1]] += 1
        # print(inAngle)
        result = [i for i in range(len(inAngle)) if inAngle[i] == 0]
        return result

# @lc code=end

