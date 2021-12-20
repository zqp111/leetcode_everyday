#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        traveled = [1]*n
        traveled[0] = 0
        keys = rooms[0]
        while keys:
            # print(keys, traveled)
            key = keys.pop(0)
            traveled[key] = 0
            newkeys = rooms[key]
            for newkey in newkeys:
                if traveled[newkey]:
                    keys.append(newkey)
            
        return sum(traveled) == 0

# @lc code=end

