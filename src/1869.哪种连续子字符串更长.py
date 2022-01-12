#
# @lc app=leetcode.cn id=1869 lang=python3
#
# [1869] 哪种连续子字符串更长
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        tmp = s[0]
        maxZero, maxOne = (0, 1) if tmp=='1' else (1, 0)
        tmpLen = 1
        for i in range(1, len(s)):
            if s[i] == tmp:
                tmpLen += 1
            else:
                tmpLen = 1
                tmp = s[i]
            if tmp == '1': maxOne = max(tmpLen, maxOne)
            else: maxZero = max(tmpLen, maxZero)
        return maxOne > maxZero

# @lc code=end

