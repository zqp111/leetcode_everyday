#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sum_nums = []
        sum_ = 0
        for num in nums:
            sum_ += num
            sum_nums.append(sum_)
        print(sum_nums)
        sum_nums.sort()
        right = 0

        def find_right(left):



        for left in range(len(sum_nums)):


# @lc code=end

