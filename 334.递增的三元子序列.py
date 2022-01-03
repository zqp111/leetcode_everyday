#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = nums[0], None
        for num in nums[1:]:
            if second is None:
                if first < num:
                    second = num
                else:
                    first = num
            elif num <= second:
                if num <= first:
                    first = num
                else:
                    second = num
            else:
                return True
            # print(first, second)
        return False
# @lc code=end

