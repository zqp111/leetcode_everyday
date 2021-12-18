#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    dp[j] += dp[i]
        return True if dp[-1] != 0 else False
# @lc code=end

