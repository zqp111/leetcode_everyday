#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        alphaDict = set()
        result = 0
        for i in range(0, len(s)):
            if s[i] in alphaDict:
                result += 2
                alphaDict.remove(s[i])
            else:
                alphaDict.add(s[i])
        return result + 1 if len(alphaDict) > 0 else result
# @lc code=end

