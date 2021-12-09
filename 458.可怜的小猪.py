#
# @lc app=leetcode.cn id=458 lang=python3
#
# [458] 可怜的小猪
#

# @lc code=start
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets <= 1:
            return 0
        A = minutesToTest//minutesToDie +1
        ans = 1
        tmp = A
        while tmp < buckets:
            tmp *= A
            ans +=1
        return ans
# @lc code=end

