#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        keyNums = dict()
        for num in arr:
            if keyNums.__contains__(num):
                keyNums[num] += 1
            else:
                keyNums[num] = 1
        ans = set()
        for _, value in keyNums.items():
            if value in ans:
                return False
            ans.add(value)
        return True

# @lc code=end

