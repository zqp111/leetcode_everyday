#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        startIdx = 0
        result = ''
        while len(s[startIdx:startIdx+2*k]) == 2*k:
            result += s[startIdx:startIdx+k][::-1]+s[startIdx+k:startIdx+2*k]
            startIdx += 2*k
        if len(s[startIdx:startIdx+2*k]) <= k:
            result += s[startIdx:startIdx+k][::-1]
        else:
            result += s[startIdx:startIdx+k][::-1]+s[startIdx+k:startIdx+2*k]
        return result
# @lc code=end

