#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for char in t: 
            if char == s[0]:
                s = s[1:]
            if len(s) == 0:
                return True
        return False

# @lc code=end

