#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if not stack or stack[-1][0] != s[i]:
                stack.append([s[i], 1])
            else:
                stack[-1][1] +=1
            if stack[-1][1] == k:
                stack.pop(-1)
        result = ''
        for i in range(len(stack)):
            result += stack[i][0]*stack[i][1]
        return result
# @lc code=end

