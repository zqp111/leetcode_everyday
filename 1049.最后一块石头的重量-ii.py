#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        numsSum = sum(stones)
        targetNum = numsSum // 2

        re = [0]*(targetNum + 1)
        for i in range(len(stones)):
            for j in range(targetNum, stones[i]-1, -1):
                re[j] = max(re[j], re[j-stones[i]]+stones[i])
        return numsSum - 2*re[-1]

# @lc code=end

