#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if len(t) != n:
            return False
        transforDict = dict()
        fSet = set()
        for i in range(n):
            if transforDict.__contains__(s[i]):
                if transforDict[s[i]] != t[i]:
                    return False
            else:
                if t[i] in fSet:
                    return False
                fSet.add(t[i])
                transforDict[s[i]] = t[i]
        
        return True
# @lc code=end 

