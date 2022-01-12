#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in operator:
                b = stack.pop(-1)
                a = stack.pop(-1)
                stack.append(self.__compute(a, b, token))
            else:
                stack.append(int(token))
            # print(stack)
        return stack.pop(-1)
    
    def __compute(self, a, b, operator):
        if operator == '+':
            return a + b
        if operator == '-':
            return a - b
        if operator == '*':
            return a * b
        if operator == '/':
            return int(a / b)
# @lc code=end

