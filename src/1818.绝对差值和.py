#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#

# @lc code=start
import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        allSum = 0
        for i in range(len(nums1)):
            allSum += abs(nums1[i] - nums2[i])
        
        sortedArr1 = sorted(nums1.copy())
        maxReduce = 0
        for i in range(len(nums1)):
            index = bisect.bisect(sortedArr1, nums2[i])
            if index != 0:
                maxReduce = max(maxReduce, abs(nums1[i] - nums2[i])-abs(sortedArr1[index-1]-nums2[i]))
            if index != len(sortedArr1):
                maxReduce = max(maxReduce, abs(nums1[i] - nums2[i])-abs(sortedArr1[index]-nums2[i]))
        return int((allSum-maxReduce)%(1e9+7))

# @lc code=end

