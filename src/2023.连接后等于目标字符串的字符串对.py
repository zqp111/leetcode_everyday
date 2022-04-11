#
# @lc app=leetcode.cn id=2023 lang=python3
#
# [2023] 连接后等于目标字符串的字符串对
#

# @lc code=start
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    ans += 1
        return ans
# @lc code=end

