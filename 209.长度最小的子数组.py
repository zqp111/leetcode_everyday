#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 1
        min_ = len(nums)+1
        while right <= len(nums):
            # print(left, right)
            if sum(nums[left:right]) > s:
                min_ = min(min_, right -left)
                if sum(nums[left+1:right]) >= s:
                    left += 1
                    continue
            elif sum(nums[left:right]) < s:
                right +=1
                continue
            else:
                min_ = min(min_, right -left)
            left += 1
            right += 1
        if min_ == len(nums)+1:
            return 0
        return min_         

# @lc code=end

