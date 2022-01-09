class Solution:
    def reverseWords(self, s: str) -> str:
        splitWords = s.split(' ')
        result = ''
        for word in splitWords[::-1]:
            if not word: continue
            result = result + ' ' + word
        return result[1:]