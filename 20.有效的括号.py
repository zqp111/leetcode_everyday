#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = set('([{')
        pair = {')': '(', ']': '[', '}':'{'}
        for char in s:
            if char in left:
                stack.append(char)
            else:
                if not stack or pair[char] != stack[-1]:
                    return False
                stack.pop(-1)
        return not len(stack)
# @lc code=end

