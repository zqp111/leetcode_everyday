#
# @lc app=leetcode.cn id=1563 lang=python3
#
# [1563] 石子游戏 V
#

# @lc code=start
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        dp = [[0]*len(stoneValue) for _ in range(len(stoneValue))]
        for i in range(len(stoneValue)-1, -1, -1) :
            for j in range(i+1, len(stoneValue)):
                for k in range(i+1, j+1):
                    l, r = sum(stoneValue[i:k]), sum(stoneValue[k:j+1])
                    # print(i, j, k, l, r)
                    if l < r:
                        a = l+dp[i][k-1]
                    elif l > r:
                        a = r+dp[k][j]
                    else:
                        a = l + max(dp[i][k-1], dp[k][j])
                    dp[i][j] = max(dp[i][j], a)
        # print(dp)
        return dp[0][-1]

# @lc code=end

