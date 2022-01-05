#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictSeen = set()
        pair = dict()

        splitWords = s.split(' ')
        if len(splitWords) != len(pattern): return False
        for i in range(len(splitWords)):
            # print(pattern, splitWords[i])
            if pair.get(pattern[i], None) is not None:
                if pair.get(pattern[i]) != splitWords[i]:
                    return False
            else:
                pair[pattern[i]] = splitWords[i]
                if splitWords[i] in dictSeen:
                    return False
                dictSeen.add(splitWords[i])
        return True
# @lc code=end

