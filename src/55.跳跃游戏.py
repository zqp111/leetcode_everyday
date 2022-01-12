#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 1

        for i in range(len(nums)):
            if step <= 0:
                return False
            step -= 1
            step = max(step, nums[i])
        return True
# @lc code=end

