#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        """
        Do not return anything, modify s in-place instead.
        """
# @lc code=end

