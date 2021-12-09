#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        nums = 0
        while n != 0:
            nums += n //5
            n = n //5
        return nums
        
# @lc code=end

