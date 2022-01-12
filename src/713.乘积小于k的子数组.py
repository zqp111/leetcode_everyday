#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        l, r = 0, 0
        tmpRe = 1
        ans = 0

        while r<len(nums):
            # print(l, r, tmpRe)
            tmpRe *= nums[r] 
            if tmpRe < k:
                r += 1
            else:
                ans += r-l
                tmpRe /= nums[r]
                if r >l: 
                    tmpRe /= nums[l]
                
                l += 1
                r = max(l, r)
        n = r-l
        
        return ans+n*(n+1)//2

# @lc code=end

