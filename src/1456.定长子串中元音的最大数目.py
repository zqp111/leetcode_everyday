#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        target = set('aeiou')
        result = 0
        for i in range(k):
            if s[i] in target:
                result += 1
        tmpNum = result
        for i in range(1, len(s)-k+1):
            if s[i-1] in target:
                tmpNum -= 1
            if s[i+k-1] in target:
                tmpNum += 1
            result = max(result, tmpNum)
        return result

# @lc code=end

