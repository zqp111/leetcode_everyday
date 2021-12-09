#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        a = dict(zip(A, [i for i in range(len(A))]))
        n = len(A) /2
        for key in a.keys():
            if A.count(key) == n:
                return key
# @lc code=end

