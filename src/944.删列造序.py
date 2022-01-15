#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for i in range(len(strs[0])):
            last = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i]< last:
                    result += 1
                    break
                last = strs[j][i]
        return result

# @lc code=end

