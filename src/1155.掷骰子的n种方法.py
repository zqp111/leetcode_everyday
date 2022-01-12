#
# @lc app=leetcode.cn id=1155 lang=python3
#
# [1155] 掷骰子的N种方法
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

    #     ## backtracking out of time
    #     self.result = 0
    #     self.backtracking(n, k, target, 0)
    #     return self.result
        
    # def backtracking(self, n, k, target, tmp): 
    #     if n == 0: 
    #         if tmp == target: 
    #             self.result += 1
    #         return
    #     if tmp + n > target: # 剪枝1,剩余的骰子每个都为1也不满足情况
    #         return 
    #     for i in range(1, k+1):
    #         if tmp + i > target: 
    #             break # 剪枝2， 当前骰子剩余点数不能取值
    #         self.backtracking(n-1, k, target, tmp+i)

        ## dp
        dp = [[0]*target for _ in range(n)]
        for i in range(min(k, target)):
            dp[0][i] = 1

        for i in range(1, n):
            for j in range(target):
                for m in range(1, k+1):
                    if j - m >= 0: 
                        dp[i][j] +=dp[i-1][j-m]
                    else: 
                        break
                dp[i][j] %= 1e9+7
        return int(dp[-1][-1])

# @lc code=end

