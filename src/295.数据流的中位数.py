#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import bisect
class MedianFinder:

    def __init__(self):
        self.arr = []


    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        mid, i = divmod(n, 2)
        if i: return self.arr[mid]
        return (self.arr[mid]+self.arr[mid-1])/2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

