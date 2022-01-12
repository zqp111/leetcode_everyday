#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in nums:
                current_len = 1
                current_num = num
                while current_num+1 in nums:
                    current_len +=1
                    current_num +=1
                max_len = max(max_len, current_len)
        return max_len
# @lc code=end

