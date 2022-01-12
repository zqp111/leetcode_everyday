#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        Is_l = False
        ans = ''
        if num < 0:
            num = -num
            Is_l = True
        while num > 0:
            ans += str(num % 7)
            num //= 7
        if Is_l:
            ans += '-'
        ans = ans[::-1]
        return ans
# @lc code=end

