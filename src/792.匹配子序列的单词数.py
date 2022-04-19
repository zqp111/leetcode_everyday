#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#

# @lc code=start

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buk = [[] for _ in range(26)]
        
        ans = 0
        #init
        for word in words:
            buk[ord(word[0]) - ord('a')].append(word[1:])
        
        
        for chr in s:
            cur_words = buk[ord(chr) - ord('a')]
            buk[ord(chr) - ord('a')] = []

            for word in cur_words:
                if word == '':
                    ans += 1
                else:
                    buk[ord(word[0]) - ord('a')].append(word[1:])
        
        return ans

# @lc code=end

