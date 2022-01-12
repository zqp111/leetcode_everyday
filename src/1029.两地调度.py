#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x: x[0] - x[1])
        n = len(costs) //2

        result = 0
        for i, cost in enumerate(costs):
            result += cost[0] if i < n else cost[1]
        return result
                
# @lc code=end

