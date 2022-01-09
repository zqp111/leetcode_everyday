#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetDict = dict()
        
        for char in t:
            if targetDict.get(char, None) is not None:
                targetDict[char] += 1
            else:
                targetDict[char] = 1
        result = ''
        l, r = 0, 0
        tmp = s[0]
        if s[0] in targetDict.keys():
            curDict = {s[0]:1}
        else:
            curDict = dict()
        while r<len(s):
            # print(tmp)
            if self.isValid(curDict, targetDict):
                if not result or len(tmp) < len(result):
                    result = tmp
                if s[l] in curDict.keys(): curDict[s[l]] -= 1
                tmp = tmp[1:]
                l += 1
            else:
                r += 1
                if r >= len(s): return result
                if s[r] in targetDict.keys(): curDict[s[r]] = curDict.get(s[r], 0)+1
                tmp = tmp + s[r]
        return result
    
    def isValid(self, cur, target):
        for key, item in target.items():
            if cur.get(key, 0) < item: return False
        return True
# @lc code=end

