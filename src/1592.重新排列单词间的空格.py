#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        # spaceCount = 0
        wordList = text.split()
        wordLen = 0
        for word in wordList:
            wordLen += len(word)
        spaceCount = len(text) - wordLen
        if len(wordList) > 1:
            space, sub = divmod(spaceCount, len(wordList)-1)
        else:
            space, sub = 0, spaceCount
        result = ''
        for i, word in enumerate(wordList):
            if i == 0:
                result += word
            else:
                result += ' '*space + word
        return result + ' '*sub
# @lc code=end

