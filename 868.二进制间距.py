#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        begin = 0
        max_ = 0
        idx = 0
        status = True
        while n:
            if n & 1:
                if status:
                    begin = idx
                    status = False
                else:
                    max_ = max(max_, idx-begin)
                    begin = idx
            n = n >> 1
            idx += 1
        return max_
# @lc code=end

