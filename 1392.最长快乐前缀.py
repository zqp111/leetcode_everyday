#
# @lc app=leetcode.cn id=1392 lang=python3
#
# [1392] 最长快乐前缀
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:

        ## 超时
    #     pre, back = self.getPossiblePreBack(s)
    #     while pre and back:
    #         if len(pre[-1]) > len(back[-1]):
    #             pre.pop(-1)
    #         elif len(pre[-1]) < len(back[-1]):
    #             back.pop(-1)
    #         else:
    #             if pre[-1] != back[-1]:
    #                 pre.pop(-1)
    #                 back.pop(-1)
    #             else:
    #                 return pre[-1]
    #     return ''

    # def getPossiblePreBack(self, s):
    #     possiblePre, possibleBack = [], []

    #     start, end = s[0], s[-1]
    #     for i in range(0, len(s)):
    #         if s[i] ==end and i != len(s)-1: possiblePre.append(s[:i+1])
    #         if s[i] ==start and i != 0: possibleBack.insert(0,s[i:])

    #     return possiblePre, possibleBack
        start, end = s[0], s[-1]
        n = len(s)
        for i in range(1, n):
            if s[i] == start and s[n-i-1] == end:
                if s[i:] == s[:n-i]: return s[i:]
        return ''
    

# @lc code=end

