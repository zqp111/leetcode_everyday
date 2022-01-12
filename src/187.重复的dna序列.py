#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10: return []

        tmp = s[:10]
        seen = set()
        seen.add(tmp)
        result = set()
        for i in range(10, len(s)):
            newStr = tmp[1:] + s[i]
            if newStr in seen:
                if newStr not in result:
                    result.add(newStr)
            else:
                seen.add(newStr)
            tmp = newStr
        return list(result)
# @lc code=end

