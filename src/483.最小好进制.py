#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        
        targetNum = int(n)

        for num in range(60, 1, -1):
            basel, baser = 2, targetNum-1
            while basel <= baser:
                base = basel + (baser-basel)//2
                nowNum = self.getNum(base, num)
                if nowNum > targetNum:
                    baser = base - 1
                elif nowNum < targetNum:
                    basel = base + 1
                else:
                    return str(base)
    def getNum(self, base, num):
        re = 0
        for i in range(num):
            re = re*base + 1
        return re

# @lc code=end

