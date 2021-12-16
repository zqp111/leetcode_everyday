#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        status = 0
        count = 0
        for char in s:
            if char == 'L':
                status += 1
            else:
                status -= 1
            if status == 0:
                count += 1
        return count
# @lc code=end

