#
# @lc app=leetcode.cn id=1332 lang=python3
#
# [1332] 删除回文子序列
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        if self.isPalindrome(s): return 1
        return 2
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True
# @lc code=end

