#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]: 
        result = [i for i in range(1, n-k)]
        l, r = n-k, n
        while l < r:
            result.append(l)
            result.append(r)
            l += 1
            r -= 1
        if l == r: result.append(l)
        return result
            
# @lc code=end

