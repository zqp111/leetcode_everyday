#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            suma = numbers[left]+numbers[right]
            if suma == target:
                return left+1, right+1
            elif suma < target:
                left += 1
            else:
                right -= 1
# @lc code=end

