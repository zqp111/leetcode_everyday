#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        maxlen = 0
        windict = {}
        while right < len(s):
            if 
# @lc code=end