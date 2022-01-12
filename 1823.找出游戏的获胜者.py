#
# @lc app=leetcode.cn id=1823 lang=python3
#
# [1823] 找出游戏的获胜者
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]
        beginIndex = 0
        while len(nums) > 1:
            beginIndex = self.dropOnePlayer(beginIndex, k, nums)
        return nums[0]

    def dropOnePlayer(self, beginIndex, k, nums):
        n = len(nums)
        selectIndex = (beginIndex+k-1)%n
        nums.pop(selectIndex)
        return selectIndex
# @lc code=end

