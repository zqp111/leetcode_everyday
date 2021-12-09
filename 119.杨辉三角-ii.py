#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def C(M, n):
            ans = 1
            for i in range(1, n+1):
                ans = ans*(M+1-i)/i
            return int(ans)
        ans = [1]*(rowIndex+1)
        for i in range(1, rowIndex//2 +1):
            ans[i] = ans[rowIndex-i]=C(rowIndex, i)
        return ans
# @lc code=end

