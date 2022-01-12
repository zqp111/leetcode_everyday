#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        for num in nums:
            tmp ^= num
        f = tmp&(-tmp)
        a = 0
        for num in nums:
            if f&num:
                a ^= num
        return [a, tmp^a]

# @lc code=end

