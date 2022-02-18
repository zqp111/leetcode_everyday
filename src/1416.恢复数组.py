#
# @lc app=leetcode.cn id=1416 lang=python3
#
# [1416] 恢复数组
#

# @lc code=start
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0]*len(s)
        dp = dp + [1]
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                for j in range(i+1, len(s)+1, 1):
                    if int(s[i:j]) <= k:
                        dp[i] += dp[j]
                    else:
                        break
                # dp[i] = 1 + sum(dp[i+1:])
            dp[i] = int(dp[i] % (1e9+7))
        # print(dp)
        return dp[0]
# @lc code=end

