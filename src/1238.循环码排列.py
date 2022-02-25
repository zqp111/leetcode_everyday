#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#

# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [start]
        for i in range(1, 2**n): 
            ans.append(i^(i>>1)^start)
        return ans
# @lc code=end

