#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wordList = self.__getWord(paragraph)
        wordDict = {}
        maxWords = 0
        result = None
        for word in wordList:

            if word in banned:
                continue

            if wordDict.get(word, None) is not None:
                wordDict[word] += 1
            else:
                wordDict[word] = 1

            if wordDict[word] > maxWords:
                    maxWords = wordDict[word]
                    result = word

        return result

    def __getWord(self, paragraph):
        tmp = ''
        wordList = []
        for char in paragraph:
            if not char.isalpha() and tmp:
                wordList.append(tmp)
                tmp = ''
            elif char.isalpha():
                tmp += char.lower()
        if tmp:
            wordList.append(tmp)
        return wordList
        
# @lc code=end

