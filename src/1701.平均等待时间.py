#
# @lc app=leetcode.cn id=1701 lang=python3
#
# [1701] 平均等待时间
#

# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        timeSum = 0
        delayTime = 0
        for arriveTime, time in customers:
            if arriveTime >= delayTime:
                timeSum += time
                delayTime = arriveTime+time
            else:
                timeSum += (time + delayTime-arriveTime)
                delayTime = delayTime + time
        return timeSum/(len(customers))
# @lc code=end

