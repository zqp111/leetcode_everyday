#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        A = s+t
        ans = 0
        for i in range(len(A)):
            ans ^=ord(A[i])
        return chr(ans)
# @lc code=end

