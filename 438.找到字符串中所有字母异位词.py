#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = [0]*26
        
        if len(s) < len(p): return []

        for i in range(len(p)):
            pDict[ord(p[i]) - ord('a')] += 1
            pDict[ord(s[i]) - ord('a')] -= 1

        ans = []
        if self.__is_same(pDict):
            ans.append(0)

        for i in range(len(s) - len(p)):
            pDict[ord(s[i]) - ord('a')] += 1
            pDict[ord(s[i+len(p)]) - ord('a')] -= 1
            if self.__is_same(pDict):
                ans.append(i+1)
        return ans

    
    def __is_same(self, pDict):
        for num in pDict:
            if num != 0:
                return False
        return True
# @lc code=end

