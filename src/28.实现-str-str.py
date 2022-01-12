#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # j = 0
        # re = 0
        # if len(needle) == 0:
        #     return 0
        # if len(needle) == len(haystack) and needle == haystack:
        #     return 0
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i

        # return -1
        return haystack.find(needle)
        
# @lc code=end

