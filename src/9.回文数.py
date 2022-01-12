#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        l, r = 0, len(string)-1
        while l < r:
            if string[l] != string[r]: return False
            l += 1
            r -= 1
        return True
# @lc code=end

