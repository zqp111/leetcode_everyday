#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        base = 1
        count = 1
        ans = 0
        tmp = n
        while tmp:
            b = n % base# 当前位之后的数值
            base *= 10
            s = tmp % 10 # 取当前位
            tmp = n // base # 当前位之前的

            if s == 0:
                # count *= 10
                ans += tmp*count
            elif s == 1:
                ans += (b+1)
                # count *= 10
                ans += tmp*count
            else:
                ans += (tmp+1)*count
            count *= 10
            
        return ans

# @lc code=end

