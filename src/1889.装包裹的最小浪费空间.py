#
# @lc app=leetcode.cn id=1889 lang=python3
#
# [1889] 装包裹的最小浪费空间
#

# @lc code=start
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        for box in boxes:
            box.sort()
        allSum = sum(packages)
        answer = 2 ** 63 - 1
        for box in boxes:
            if box[-1] < packages[-1]:
                continue
            ptr = 0
            cur = 0
            for aBox in box:
                curPtr = bisect.bisect_right(packages, aBox)
                cur += (curPtr - ptr) * aBox
                ptr = curPtr
            answer = min(answer, cur - allSum) # 缓存所有的元素之和，避免重复计算
        return answer % (10 ** 9 + 7) if answer != 2 ** 63 - 1 else -1
# @lc code=end
