#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1Index, num2Index = len(num1)-1, len(num2)-1

        re = ''

        c = 0

        while num1Index >= 0 and num2Index >= 0:
            n = int(num1[num1Index]) + int(num2[num2Index]) + c
            c, n = divmod(n, 10)

            re = str(n) + re
            num1Index -= 1
            num2Index -= 1

        if num1Index < 0: # 第一个字符串结束
            while num2Index >= 0:
                n = int(num2[num2Index]) + c
                c, n = divmod(n, 10)

                re = str(n) + re
                num2Index -= 1
        else:
            while num1Index >= 0:
                n = int(num1[num1Index]) + c
                c, n = divmod(n, 10)

                re = str(n) + re
                num1Index -= 1
        if c:
            re = str(c) + re
        return re

# @lc code=end

