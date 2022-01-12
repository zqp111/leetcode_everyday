#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        newArray = []
        for num in arr:
            newArray.append([self._get1Num(num), num])
        newArray.sort()
        # print(newArray)

        return [num[1] for num in newArray]
    
    def _get1Num(self, num):
        count = 0
        while num:
            count += num%2
            num = num >> 1
        return count
# @lc code=end

