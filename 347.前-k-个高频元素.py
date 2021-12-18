#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = dict()
        for num in nums:
            if a.__contains__(num):
                a[num] += 1
            else:
                a[num] = 1
        a_sorted = sorted(a.items(), key=lambda m: m[1], reverse=True)
        return [a_sorted[i][0] for i in range(k)]
# @lc code=end

