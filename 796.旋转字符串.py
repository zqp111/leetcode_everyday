#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        for i in range(0, len(A)): 
            if A[i] == B[0]:
                if A[i:] + A[:i] == B:
                    return True
        return False
# @lc code=end

