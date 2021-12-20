#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            if i == 0:
                l_sum += 0
            else:
                l_sum += nums[i-1]
            r_sum -= nums[i]
            # print(l_sum, r_sum, i)
            if l_sum == r_sum:
                return i
            
        return -1
# @lc code=end

