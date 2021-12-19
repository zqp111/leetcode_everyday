#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        
        splitedWords = []
        tmpWords = ""
        for char in s:
            if char == ' ':
                if tmpWords:
                    splitedWords.append(tmpWords)
                    tmpWords = ""
            else:
                tmpWords += char
        if tmpWords:
            splitedWords.append(tmpWords)
        
        result = ""
        for i in range(len(splitedWords)-1 , -1, -1):
            result +=splitedWords[i]+' '
        return result[:-1]


# @lc code=end

