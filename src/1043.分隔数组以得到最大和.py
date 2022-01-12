#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*(len(arr)+1)
        dp[-2] = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            for j in range(i, min(i+k,len(arr))):
                dp[i] =max(dp[i], max(arr[i:j+1])*(j-i+1) + dp[j+1])
        # print(dp)
        return dp[0]
# @lc code=end

