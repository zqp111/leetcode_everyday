#
# @lc app=leetcode.cn id=1739 lang=python3
#
# [1739] 放置盒子
#

# @lc code=start
import math
class Solution:
    def minimumBoxes(self, n: int) -> int:
        result = 0
        tmp = 0
        boxcount = 0
        while boxcount < n:
            tmp += 1
            result += tmp
            boxcount += result
            # print(boxcount)
        if boxcount == n: return result

        boxcount -= result
        result -= tmp
        res = n - boxcount

        addbox = 0
        for i in range(1, tmp+1):
            res -= i
            addbox += 1
            if res <= 0: break
        return result + addbox
# @lc code=end

