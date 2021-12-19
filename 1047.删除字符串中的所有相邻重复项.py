#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 2:
            return s
        l, r = 0, 1
        while True:
            if s[l] == s[r]:
                s = s[:l] + s[r+1:]
                if l != 0:
                    r = l
                    l -= 1
            else:
                l = r
                r += 1
            if r >= len(s):
                break
        return s
        
# @lc code=end

