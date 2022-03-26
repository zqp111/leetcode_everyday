#
# @lc app=leetcode.cn id=789 lang=python3
#
# [789] 逃脱阻碍者
#

# @lc code=start
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = abs(target[0]) + abs(target[1])
        for g in ghosts:
            if abs(g[0] - target[0]) + abs(g[1] - target[1]) <= d:
                return False
        return True
# @lc code=end

