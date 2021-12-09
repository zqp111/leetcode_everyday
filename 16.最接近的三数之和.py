#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # if len(nums) == 3:
        #     return nums[0] + nums[1] + nums[2]
        nums.sort()
        # print(nums)
        
        min_error = 1000000
        for p in range(len(nums)):
            l, r = 0, len(nums) - 1
            while l < r:
                if l == p:
                    l += 1
                elif r == p:
                    r -= 1
                else:
                    current_error = nums[p]+nums[l]+nums[r]-target
                    if current_error > 0:
                        r -= 1
                    elif current_error < 0:
                        l += 1
                    else:
                        return target
                    if abs(current_error) < abs(min_error):
                        min_error = current_error
        return min_error+target
                

# @lc code=end

