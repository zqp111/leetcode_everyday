#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:


        # ## dp 超时
        # dp = [ [ [0]*(len(cardPoints)) for _ in range(len(cardPoints))] for _ in range(k+1)]
        # for i in range(len(cardPoints)):
        #     for k_i in range(1, k+1):
        #         dp[k_i][i][i] = cardPoints[i]

        # for i in range(len(cardPoints)-2, -1, -1):
        #     for j in range(i+1, len(cardPoints)):
        #         for k_i in range(1, k+1):
        #             dp[k_i][i][j] = max(dp[k_i-1][i+1][j] + cardPoints[i], dp[k_i-1][i][j-1] + cardPoints[j])
        
        # # print(dp[0])
        # return dp[-1][0][-1]

        ## 滑窗
        l, r = 0, len(cardPoints) - k
        tmpSum = sum(cardPoints[l:r])
        minSum = tmpSum
        for i in range(k):
            
            tmpSum -= cardPoints[l]
            tmpSum += cardPoints[r]
            minSum = min(minSum, tmpSum)
            l +=1
            r +=1
        return sum(cardPoints) - minSum


# @lc code=end

