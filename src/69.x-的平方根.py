#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                right = mid-1
            else:
                left = mid+1
        return right
# @lc code=end

