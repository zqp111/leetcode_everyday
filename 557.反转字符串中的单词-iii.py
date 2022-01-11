#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        result = ''
        for word in words:
            result += " "+word[::-1]
        return result[1:]


# @lc code=end

