#
# @lc app=leetcode.cn id=2111 lang=python3
#
# [2111] 使数组 K 递增的最少操作次数
#

# @lc code=start
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        result = 0
        for i in range(k):
            tmpLen = 0
            minEnd = []
            for j in range(i, len(arr), k):
                tmpLen += 1
                if not minEnd: minEnd.append(arr[j])
                else:
                    index = bisect_right(minEnd, arr[j])
                    if index == len(minEnd):
                        minEnd.append(arr[j])
                    else:
                        minEnd[index] = arr[j]
            result += tmpLen - len(minEnd)
        return result
# @lc code=end

