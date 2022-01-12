#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        isOne = [0] * len(isConnected)
        self.result = 0
        for i in range(len(isConnected)):
            self.getConnected(i, isOne, isConnected)
        return self.result

    def getConnected(self, i, isOne, isConnected):
        if isOne[i] != 0:
            return
        self.result += 1
        stack = [i]
        while stack:
            cur = stack.pop()
            isOne[cur] = 1
            for j in range(len(isConnected[cur])):
                if isConnected[cur][j] and not isOne[j]:
                    stack.append(j)


# @lc code=end

