#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 500*25: return 1
        memory = {}
        return self.getAnswer(n, n, memory)
        
    def getAnswer(self, a, b, memory):
        if memory.get((a, b), None) is None:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            memory[(a, b)] = sum([self.getAnswer(a-100, b, memory),
                            self.getAnswer(a-75, b-25, memory),
                            self.getAnswer(a-50, b-50, memory),
                            self.getAnswer(a-25, b-75, memory)])/4.0
        return memory[(a, b)]
# @lc code=end

