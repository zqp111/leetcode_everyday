#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: 
            nums1[:n] = nums2[:n]
            return
        elif n == 0:return

        l, r = m-1, n-1
        # index = m+n-1
        while l >= 0 and r >= 0:
            if nums1[l]>nums2[r]:
                nums1[l+r+1] = nums1[l]
                l -= 1
            else:
                nums1[l+r+1] = nums2[r]
                r -= 1
        if r != -1: nums1[:r+1] = nums2[:r+1]
            
# @lc code=end

