#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后K个零
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        if K == 0:
            return 5
        def get_k(n):
            ans = n
            while n:
                n = n//5
                ans += n
            return ans
        N = -1
        q = K
        while q:
            q = q//5
            N +=1
        # print(N)
        M = 0
        for i in range(0, N+1):
            M += 5**i
        # print(K*(5**N), M)
        h = ceil(K*(5**N)/M)
        for i in range(h, h+25):
            if get_k(i) == K:
                return 5
        return 0

# @lc code=end

