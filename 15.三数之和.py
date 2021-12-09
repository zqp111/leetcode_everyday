#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        result = []
        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            if (i != 0) and (nums[i] == nums[i - 1]):
                continue
            while l < r:
                if (l != i+1) and (nums[l] == nums[l-1]):
                    l += 1
                elif (r != n-1) and (nums[r] == nums[r+1]):
                    r -= 1
                else:
                    tmp  = nums[l] + nums[r] + nums[i]
                    if tmp == 0:
                        result.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif tmp > 0:
                        r -= 1
                    else:
                        l += 1
        return result
                    
# @lc code=end

