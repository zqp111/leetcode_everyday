#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x!= 0 or y!= 0:
            result += ((x&1)^(y&1) != 0)
            x = x >> 1
            y = y >> 1
        return result

# @lc code=end

