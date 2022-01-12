#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp = nums[0]
        p = 1
        for num in nums[1:]:
            
            if num == tmp:
                p += 1
            elif p and num != tmp:
                p -= 1
            else:
                tmp = num
                p = 1
            # print(tmp, p)
        return tmp
# @lc code=end

