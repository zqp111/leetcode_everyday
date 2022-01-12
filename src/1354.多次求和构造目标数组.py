#
# @lc app=leetcode.cn id=1354 lang=python3
#
# [1354] 多次求和构造目标数组
#
import heapq

# @lc code=start
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # 无加速，超时
        targetSum = sum(target)
        heap = []
        n = len(target)
        for i in range(n):
            heapq.heappush(heap, -target[i])
        while True:
            # print(heap)
            maxNum = heapq.heappop(heap)
            if maxNum == -1:
                return True
            targetSum += maxNum
            if targetSum == 0:
                return False
            newNum = targetSum + maxNum
            if newNum >= 0:
                return False

            newNum = -((-newNum) % targetSum) ## 这里进行加速
            
            
            if newNum == 0:
                newNum = -targetSum
            # print(newNum)
            # if newNum == maxNum:
            #     return False

            targetSum -=newNum
            heapq.heappush(heap, newNum)
# @lc code=end

