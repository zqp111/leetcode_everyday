#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        dic = [0]*10
        color2i = {'R': 1, 'G': 2, 'B': 4}
        for i in range(0, len(rings), 2):
            color, index = color2i[rings[i]], int(rings[i+1])
            dic[index] |= color
        result = 0
        for i in range(10):
            if dic[i] == 7:
                result += 1
        return result
# @lc code=end

