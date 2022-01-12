#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in range(len(s)):
            if s[i] != '#':
                s_stack.append(s[i])
            elif s_stack:
                s_stack.pop(-1)
        for i in range(len(t)):
            if t[i] != '#':
                t_stack.append(t[i])
            elif t_stack:
                t_stack.pop(-1)
        if len(t_stack) != len(s_stack):
            return False
        for i in range(len(s_stack)):
            if s_stack[i] != t_stack[i]:
                return False
        return True
# @lc code=end

