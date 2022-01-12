#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        result = [0, 0]
        dic = {'R':(0, 1), 'L':(0, -1), 'U':(1, 1), 'D':(1, -1)}

        for c in moves:
            result[dic[c][0]] += dic[c][1]
        return True if result == [0, 0] else False
# @lc code=end

