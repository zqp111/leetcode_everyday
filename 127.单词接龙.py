#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [beginWord]
        closeSet = set()
        path = 1
        while queue:
            length = len(queue)
            path += 1
            for i in range(length):
                curWord = queue.pop(0)
                j = 0
                while j != len(wordList):
                    if self.__canTransfer(curWord, wordList[j]):
                        # print(wordList[j])
                        if wordList[j] == endWord:
                            return path
                        queue.append(wordList.pop(j))
                    else:
                        j += 1
        return 0

    def __canTransfer(self, word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
        return count == 1

# @lc code=end

