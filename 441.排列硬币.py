#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        A = int(sqrt(2*n))
        if A*(A+1)/2 > n:
            return A-1
        return A
# @lc code=end

