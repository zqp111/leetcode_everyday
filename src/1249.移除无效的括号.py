#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        popStack = []
        for i in range(len(s)):
            if s[i] == '(': popStack.append(i)
            elif s[i] == ')':
                if not popStack or s[popStack[-1]] == ')':
                    popStack.append(i)
                else:
                    popStack.pop(-1)
        for index in popStack[::-1]:
            s = s[:index] + s[index + 1:]
        return s
# @lc code=end

