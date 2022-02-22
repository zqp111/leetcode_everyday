#
# @lc app=leetcode.cn id=1754 lang=python3
#
# [1754] 构造字典序最大的合并字符串
#

# @lc code=start
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        a, b = word1, word2
        res = ""
        while a and b:
            if a > b:
                res += a[0]
                a = a[1:]
            else:
                res += b[0]
                b = b[1:]
        return res + a + b
# @lc code=end

