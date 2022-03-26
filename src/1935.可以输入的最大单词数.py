#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenSet = set(brokenLetters)
        words = text.split(' ')
        res = 0
        for word in words:
            if set(word) & brokenSet == set():
                res += 1
        return res
# @lc code=end

