#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # if jug1Capacity + jug2Capacity == targetCapacity:
        #     return True
        # elif jug1Capacity + jug2Capacity < targetCapacity:
        #     return False
        # elif targetCapacity > max(jug1Capacity, jug2Capacity):
        #     return self.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity-jug1Capacity) or self.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity-jug2Capacity)
        
        # x = min(jug1Capacity, jug2Capacity)

        # open_list = [x]
        # close_list = [jug1Capacity, jug2Capacity]

        # while len(open_list) > 0:
        #     # print(open_list, close_list)
        #     if targetCapacity in close_list:
        #         return True

        #     now_s = open_list.pop(0)

        #     for jug in close_list:
        #         m = jug-now_s
        #         # print(m)
        #         if m > 0 and m not in close_list:
        #             # print(m)
        #             open_list.append(m)
        #             close_list.append(m)
        # if targetCapacity in close_list:
        #     return True
        # return False

        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity == 0 or jug1Capacity + jug2Capacity == targetCapacity
        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0
# @lc code=end

