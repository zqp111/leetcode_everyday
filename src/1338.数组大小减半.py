#
# @lc app=leetcode.cn id=1338 lang=python3
#
# [1338] 数组大小减半
#

# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = dict()
        for num in arr:
            count[num] = count.get(num, 0) + 1

        n = len(arr)/2
        countNums = list(count.values())
        countNums.sort(reverse=True)
        sumcount = 0
        for i in range(len(countNums)):
            sumcount += countNums[i]
            if sumcount >= n: 
                return i+1
            

# @lc code=end

