#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        re1,im1 = int(a.split("+")[0]), int(a.split("+")[1][:-1])
        re2,im2 = int(b.split("+")[0]), int(b.split("+")[1][:-1])
        ansr = re1*re2 - im1*im2
        ansi = re1*im2 + re2*im1
        return str(ansr) +'+'+ str(ansi) + 'i'
# @lc code=end

