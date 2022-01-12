#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ''
        for word in dictionary:
            if self.__isSub(s, word):
                if (len(word) > len(res)) or (len(word) == len(res) and word < res):
                    res = word
        return res 


    def __isSub(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word): 
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)
# @lc code=end

