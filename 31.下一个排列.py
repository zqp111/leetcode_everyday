#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    # print(i, j, nums)
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:] = sorted(nums[i+1:])
                    return
        else:
            nums[:] = nums[::-1]
# @lc code=end

