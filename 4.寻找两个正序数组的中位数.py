#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        mid, f = divmod(n1+n2, 2)
        mid = mid-1+f
        index1, index2 = 0, 0
        last = None
        while index1+index2 -1<= mid:
            
            if index1+index2-1 == mid:
                midNum = last
            if index1 >= n1 and index2 >= n2: break
            elif index1 >= n1:
                last = nums2[index2]
                index2 += 1
            elif index2>=n2 or nums1[index1] < nums2[index2]:
                last = nums1[index1]
                index1 += 1
            else:
                last = nums2[index2]
                index2 += 1
            # print(index1, index2, last)
        # print(midNum, last)
        if f: return midNum
        else: 
            return (midNum+last)/2
# @lc code=end

