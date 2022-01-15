#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#

# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        status = 0
        l = 0
        # index = 1
        for index in range(1, len(arr)):
            if status == 0:
                if arr[index] > arr[index - 1]:
                    status = 1
                else:
                    l = index
            elif status == 1:
                if arr[index] < arr[index - 1]:
                    status = 2
                elif arr[index] == arr[index - 1]:
                    l = index
                    status = 0
            elif status == 2:
                if arr[index] > arr[index - 1]:
                    result = max(result, index - l)
                    l = index-1
                    status = 1
                elif arr[index] == arr[index - 1]:
                    result = max(result, index - l)
                    l = index
                    status = 0
        if status == 2:
            result = max(result, len(arr) - l)
        return result


# @lc code=end

