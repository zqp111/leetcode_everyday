#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        begin = 0

        while begin < N:
            tmp = 0
            for i in range(begin, begin+N):
                tmp += gas[i if i < N else i-N]-cost[i if i < N else i-N]
                if tmp < 0:
                    begin = i + 1
                    break
            if i == begin+N-1:
                return begin
        return -1
# @lc code=end

