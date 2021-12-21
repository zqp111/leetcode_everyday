#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif arr[i] < arr[i-1]:
                break
            up = 1
        if i == 1:
            return False
        for j in range(i, len(arr)):
            if arr[j] >= arr[j-1]:
                return False
        return True

# @lc code=end

