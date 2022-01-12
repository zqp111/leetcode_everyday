#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ## heap
        # a = nums[:k]
        # heapq.heapify(a)
        # # print(a)
        # for num in nums[k:]:
        #     if num > a[0]:
        #         heapq.heapreplace(a, num)
        #     # print(a)
        # return a[0]
        return self.find(nums, 0, len(nums)-1, k)

    def find(self, nums, l, r, k):
        index = self.quickselect(nums, l, r)
        # print(nums, index)
        if index == k-1:
            return nums[index]
        elif index < k:
            return self.find(nums, index+1, r, k)
        else:
            return self.find(nums, l, index-1, k)

    def quickselect(self, nums, l ,r):
        index = random.choice(range(l, r+1))
        # print('choice:', index)
        nums[index], nums[r] = nums[r], nums[index]

        j = l
        for i in range(l, r):
            if nums[i] > nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[r] = nums[r], nums[j]
        return j

# @lc code=end

