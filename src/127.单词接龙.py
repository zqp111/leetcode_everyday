#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [beginWord]
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
    #     self.buildEdge(beginWord, wordList)

    #     queue = [beginWord]
    #     path = 1
    #     while queue:
    #         length = len(queue)
    #         path += 1
    #         for i in range(length):
    #             curWord = queue.pop(0)
    #             j = 0
    #             while j != len(wordList):
    #                 if self.canTransfer(curWord, wordList[j]):
    #                     # print(wordList[j])
    #                     if wordList[j] == endWord:
    #                         return path
    #                     queue.append(wordList.pop(j))
    #                 else:
    #                     j += 1
    #     return 0
    # def canTransfer(self, word1, word2):
    #     return self.Edge[self.worddict[word1]][self.worddict[word2]]

    # def __canTransfer(self, word1, word2):
    #     count = 0
    #     for i in range(len(word1)):
    #         if word1[i] != word2[i]:
    #             count += 1
    #     return count == 1

    # def buildEdge(self, beginWord, wordList):
    #     self.Edge = [[0]*(len(wordList)+1) for _ in range(len(wordList)+1)]
    #     all = [beginWord] + wordList
    #     for i in range(len(all)):
    #         for j in range(i+1, len(all)):
    #             self.Edge[i][j] = self.Edge[j][i] = self.__canTransfer(all[i], all[j])
    #     # for i, v in enumerate(all):
    #         # print(i, v)
    #     self.worddict = dict([(v,i) for i, v in enumerate(all)])

# @lc code=end

