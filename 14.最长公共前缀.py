#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        index = 0
        while True:
            if index >= len(strs[0]): return result
            tmp = strs[0][index]
            for i in range(1, len(strs)):
                if index >= len(strs[i]) or strs[i][index] != tmp:
                    return result
            result += tmp
            index += 1
# @lc code=end

