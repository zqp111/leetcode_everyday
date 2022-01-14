#
# @lc app=leetcode.cn id=1326 lang=python3
#
# [1326] 灌溉花园的最少水龙头数目
#

# @lc code=start
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        prev = [x for x in range(n + 1)]
        for i in range(n + 1):
            l = max(i - ranges[i], 0)
            r = min(i + ranges[i], n)
            prev[r] = min(prev[r], l)
        
        breakpoint, furthest = n, 2**30
        ans = 0
        for i in range(n, 0, -1):
            furthest = min(furthest, prev[i])
            if i == breakpoint:
                if furthest >= i:
                    return -1
                breakpoint = furthest
                ans += 1
        
        return ans
# @lc code=end

