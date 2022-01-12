#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i, temperature in enumerate(temperatures):
            
            while stack and stack[-1][1] < temperature:
                idx = stack.pop(-1)[0]
                result[idx] = i - idx
            stack.append((i, temperature))
        return result


# @lc code=end

