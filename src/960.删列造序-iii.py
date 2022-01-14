#
# @lc app=leetcode.cn id=960 lang=python3
#
# [960] 删列造序 III
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [1]*len(strs[0])
        result = 1
        for i in range(1, len(strs[0])):
            for j in range(i):
                if self.iscan(strs, i, j):
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        # print(dp)
        return len(strs[0])-result
        
    def iscan(self, strs, i, j):
        for str in strs:
            if str[i] < str[j]: return False
        return True

# @lc code=end

