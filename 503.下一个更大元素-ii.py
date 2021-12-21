#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1]*n
        stack = []
        for i in range(2*n):
            i %= n
            while stack and nums[i] > stack[-1][0]:
                result[stack.pop()[1]] = nums[i]
            stack.append((nums[i], i))
        return result

# @lc code=end

