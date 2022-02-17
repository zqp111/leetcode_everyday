#
# @lc app=leetcode.cn id=853 lang=python3
#
# [853] 车队
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = dict()
        for i in range(len(position)):
            t[position[i]] = (target-position[i])/speed[i]
        position.sort(reverse=True)
        result = 1
        for p in range(1, len(position)):
            if t[position[p]] <= t[position[p-1]]:
                t[position[p]] = t[position[p-1]]
            else:
                result += 1
        return result
# @lc code=end

