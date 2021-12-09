#
# @lc app=leetcode.cn id=798 lang=python3
#
# [798] 得分最高的最小轮调
#

# @lc code=start
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        N = len(A)
        bad_socares = [0] * N
        for i in range(N):
            left, right=(i-A[i]+1)%N, (i+1)%N
            bad_socares[left] -= 1
            bad_socares[right] += 1
            if left > right:
                bad_socares[0] -= 1
        
        max_ = -N
        current, ans = 0, 0
        for i in range(N):
            current += bad_socares[i]
            if current > max_:
                max_ = current
                ans = i
        return ans
        
# @lc code=end

