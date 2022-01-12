#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        while True:
            a, b=0, 0
            N = 0
            for i in range(len(nums)):
                if nums[i]:
                    N = 1
                if nums[i]&1:
                    b +=1
                else:
                    a +=1
                nums[i] >>= 1
            if N == 0:
                return ans
            ans += a*b
# @lc code=end

