#
# @lc app=leetcode.cn id=1593 lang=python3
#
# [1593] 拆分字符串使唯一子字符串的数目最大
#

# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 0
        seen = set()
        self.backtracking(s, seen)
        return self.result

    def backtracking(self, s, seen):
        if not s:
            self.result = max(self.result, len(seen))
        
        if self.result >= len(seen) + len(s):
            return

        for i in range(1, len(s)+1):
            if s[:i] not in seen:
                seen.add(s[:i])
                self.backtracking(s[i:], seen)
                seen.remove(s[:i])

# @lc code=end

