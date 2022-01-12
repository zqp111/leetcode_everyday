#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            if dictionary.__contains__(num):
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        sum = 0
        for key in sorted(dictionary.keys()):
            tmp = sum
            sum += dictionary[key]
            dictionary[key] = tmp
        # print(dictionary.keys())
        # print(nums)
        re = [dictionary[key] for key in nums]
        return re
        
# @lc code=end

