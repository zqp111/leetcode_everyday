#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = set(jewels)
        result = 0
        for stone in stones:
            if stone in jew:
                result += 1
        return result
# @lc code=end

