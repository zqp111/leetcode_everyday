#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        m = [0, 0, 0]
        for l in s:
            if l =='(': 
                m[0] += 1
            elif l ==')':
                m[0] -= 1
            elif l =='[':
                m[1] += 1
            elif l ==']':
                m[1] -= 1
            elif l =='{':
                m[2] += 1
            elif l =='}':
                m[2] -= 1
        return m == [0, 0, 0] 
# @lc code=end

