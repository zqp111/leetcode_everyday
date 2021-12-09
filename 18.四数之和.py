#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        n = len(nums)
        for i in range(n):
            
            if (i != 0) and (nums[i] == nums[i - 1]):
                continue
            for j in range(i+1, n):
                if (j != i+1) and (nums[j] == nums[j - 1]):
                    continue
                l = j+1
                r = n-1
                while l < r:
                    if (l != j+1) and (nums[l] == nums[l-1]):
                        l += 1
                    elif (r != n-1) and (nums[r] == nums[r+1]):
                        r -= 1
                    else:
                        tmp  = nums[l] + nums[r] + nums[i] + nums[j]
                        if tmp == target:
                            result.append([nums[i], nums[j], nums[l], nums[r]])
                            l += 1
                            r -= 1
                        elif tmp > target:
                            r -= 1
                        else:
                            l += 1
        return result
# @lc code=end

