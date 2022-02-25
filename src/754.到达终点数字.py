#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#

# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        
        # bfs 超时
        # queue = [0]
        # ans = 0

        # while True:
        #     ans += 1
        #     level = len(queue)
        #     for _ in range(level):
        #         cur = queue.pop(0)
        #         if cur + ans == target:
        #             return ans
        #         queue.append(cur + ans)
        #         if cur - ans == target:
        #             return ans
        #         queue.append(cur - ans)
        
        
        # math
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2
# @lc code=end

