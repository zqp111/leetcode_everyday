#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        maxlen = 1
        last = nums[0]
        curLen = 1
        for i in range(1, len(nums)) :
            if nums[i] > last:
                curLen += 1
            else:
                maxlen = max(maxlen, curLen)
                curLen = 1
            last = nums[i]
        maxlen = max(maxlen, curLen)
        return maxlen
# @lc code=end

