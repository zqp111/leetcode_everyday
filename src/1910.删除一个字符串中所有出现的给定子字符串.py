#
# @lc app=leetcode.cn id=1910 lang=python3
#
# [1910] 删除一个字符串中所有出现的给定子字符串
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        res = ""
        for ch in s:
            # 模拟从左至右匹配的过程
            res += ch
            if len(res) >= m and res[-m:] == part:
                # 如果匹配成功，那么删去对应后缀
                res = res[:-m]
        return res
# @lc code=end

