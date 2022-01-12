#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for s in ransomNote:
            id = magazine.find(s)
            if id == -1:
                return False
            magazine = magazine[:id] + magazine[id+1:]
        return True
# @lc code=end

