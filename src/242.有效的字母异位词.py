#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        sDict = dict()
        tDict = dict()
        for i in range(0, len(s)):
            if sDict.get(s[i], None) is None:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] += 1
        for i in range(0, len(t)):
            if tDict.get(t[i], None) is None:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
        for key in sDict.keys():
            if tDict.get(key, None) is None or tDict[key] != sDict[key]:
                return False
        return True
# @lc code=end

