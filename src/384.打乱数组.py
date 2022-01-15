#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        tmp = self.nums.copy()
        random.shuffle(tmp)
        return tmp



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

