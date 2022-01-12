#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        known_set = set()

        while n != 1 and n not in known_set:
            if n < 243:
                known_set.add(n)    
            n = self.__getsum(n)
        
        return n == 1
    
    def __getsum(self, n):
        ans = 0
        while n > 0:
            n, n_mod = divmod(n, 10)
            ans += n_mod**2
        return ans

# @lc code=end

