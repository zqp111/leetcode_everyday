#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        dictnum = [[] for _ in range(30)]
        for word in words:
            dictnum[len(word)-1].append(word)

        if not dictnum[0]: return ''
        last= dictnum[0]
        for i in range(1, len(dictnum)):
            if not dictnum[i]: break
            nowAvilable = []
            for word in dictnum[i]:
                if word[:-1] in last:
                    nowAvilable.append(word)
            if not nowAvilable: break
            last= nowAvilable
        last.sort()
        return last[0]

# @lc code=end

