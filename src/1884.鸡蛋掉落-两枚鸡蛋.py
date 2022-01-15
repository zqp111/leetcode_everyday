#
# @lc app=leetcode.cn id=1884 lang=python3
#
# [1884] 鸡蛋掉落-两枚鸡蛋
#

# @lc code=start
class Solution:
    def twoEggDrop(self, n: int) -> int:
        result = 0
        tmp = 0
        while n > tmp:
            n -= tmp
            tmp += 1
            result += 1
        return result
# @lc code=end

