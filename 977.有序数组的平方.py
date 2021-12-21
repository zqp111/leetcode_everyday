#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
        else:
            return [num**2 for num in nums[::-1]]
        
        if i == 0:
            return [num**2 for num in nums]
        
        l, r = i-1, i

        result = []
        l_nums = nums[l]**2
        r_nums = nums[r]**2
        while l != -1 or r != len(nums):
            if l_nums > r_nums:
                result.append(r_nums)
                r += 1
                if r == len(nums):
                    r_nums = float('inf')
                else:
                    r_nums  = nums[r]**2
            else:
                result.append(l_nums)
                l -= 1
                if l == -1:
                    l_nums = float('inf')
                else:
                    l_nums  = nums[l]**2
        return result
            

# @lc code=end

