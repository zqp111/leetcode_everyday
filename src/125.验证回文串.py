#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        l, r =0, len(s)-1

        while l < r:
            # print(l, r)
            if not (s[l].isalpha() or s[l].isdigit()):
                # print(l)
                l += 1
                continue
            if not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
                continue
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True
# @lc code=end

