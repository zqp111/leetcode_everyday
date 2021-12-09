#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        re = [[0 for _ in range(n) ]for _ in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                cost_min = i+l//2+1 + max(re[i][i+l//2-1], re[i+l//2+1][i+l])
                for j in range(i+l//2, i+l):
                    cost = j+1 + max(re[i][j-1], re[j+1][i+l])
                    cost_min = min(cost, cost_min)
                re[i][i+l] = cost_min
        print(re)
        return re[0][n-1]
# @lc code=end

