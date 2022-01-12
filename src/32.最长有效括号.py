#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        result = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i]== ')':
                stack.pop(-1)
                if stack: 
                    
                    result = max(result, i-stack[-1])
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return result
# @lc code=end

