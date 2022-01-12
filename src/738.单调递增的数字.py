#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        nums = self.get_nums(n)
        result = []

        for i in range(len(nums)-1):
            result.append(nums[i])
            if nums[i] > nums[i+1]:
                break
        else:
            return n

        while result:
            result[-1] -=1
            if len(result) == 1:
                # print(result)
                break
            elif result[-1] >= result[-2]:
                # print(result)
                break
            else:
                result.pop(-1)

        re = 0
        for i in range(len(nums)):
            if i < len(result):
                re = re*10 + result[i]
            else:
                re = re*10 + 9
        return re
    
    def get_nums(self, n):
        nums = []
        while n: 
            n, m = divmod(n, 10)
            nums.insert(0, m)
        return nums
# @lc code=end

