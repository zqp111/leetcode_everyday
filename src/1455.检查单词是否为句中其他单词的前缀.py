#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        splitedWords = sentence.split(' ')
        for i, word in enumerate(splitedWords):
            if self.isPre(searchWord, word):
                return i+1
        return -1
    
    def isPre(self, searchWord, word: str) -> bool:
        if len(searchWord) > len(word): return False
        for i in range(len(searchWord)):
            if searchWord[i] != word[i]: return False
        return True
# @lc code=end

