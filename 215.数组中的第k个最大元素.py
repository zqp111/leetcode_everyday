#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = nums[:k]
        heapq.heapify(a)
        # print(a)
        for num in nums[k:]:
            if num > a[0]:
                heapq.heapreplace(a, num)
            # print(a)
        return a[0]

# @lc code=end

