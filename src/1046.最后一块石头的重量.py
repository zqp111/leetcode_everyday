#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = []
        for m in stones:
            heapq.heappush(a, -m)
        while len(a) > 1:
            x=heapq.heappop(a)
            y=heapq.heappop(a)
            if x != y:
                heapq.heappush(a, x-y)
        if len(a) == 0:
            return 0
        else:
            return -a[0]
        
# @lc code=end

