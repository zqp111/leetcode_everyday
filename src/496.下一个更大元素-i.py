#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        numDict = dict()
        savedMax = []
        for i in range(len(nums2)-1, -1, -1):
            if len(savedMax) == 0:
                savedMax.append(nums2[i])
                numDict[nums2[i]] = -1
            else:
                while savedMax:
                    if nums2[i] < savedMax[-1]:
                        numDict[nums2[i]] = savedMax[-1]
                        savedMax.append(nums2[i])
                        break
                    else:
                        savedMax.pop(-1)
                if len(savedMax) == 0:
                    savedMax.append(nums2[i])
                    numDict[nums2[i]] = -1
        return [numDict[num] for num in nums1]
# @lc code=end

