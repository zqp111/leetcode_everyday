#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        tmp = None
        for i in range(1, len(arr)):
            if not tmp: tmp = arr[i] - arr[i-1]
            elif tmp != arr[i]-arr[i-1]: return False
        return True

# @lc code=end

