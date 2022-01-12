#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = set()
        ans = []
        for x in nums:
            if x in a:
                ans.append(x)
            else:
                a.add(x)
        for i in range(1, len(nums)+1):
            if i not in a:
                ans.append(i)
                return ans

# @lc code=end

