#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for i in range(len(g)):
            if not s:
                break
            while s and g[i] > s[0]:
                s.pop(0)
            if not s:
                break
            else:
                count += 1
                s.pop(0)
        return count
# @lc code=end

