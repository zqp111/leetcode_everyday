#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        n, c = 0, 0
        lenA = len(a)
        lenB = len(b)
        if lenA > lenB:
            b = '0'*(lenA-lenB) +b
        else:
            a = '0'*(lenB-lenA) +a
        maxLen = max(lenA, lenB)
        for i in range(maxLen-1, -1, -1):
            m = int(a[i]) + int(b[i]) + c
            c, n = divmod(m, 2)
            result = str(n) + result
        if c:
            result = str(c) + result
        return result



# @lc code=end

