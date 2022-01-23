#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while stack or pushed:
            if not stack or stack[-1] != popped[0]:
                stack.append(pushed.pop(0))
            else:
                stack.pop(-1)
                popped.pop(0)
            if not pushed and stack and stack[-1] != popped[0]:
                return False
        return True
        
# @lc code=end

