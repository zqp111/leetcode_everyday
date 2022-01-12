#
# @lc app=leetcode.cn id=2106 lang=python3
#
# [2106] 摘水果
#

# @lc code=start
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        h = deque([])
        res = 0
        n = len(fruits)
        p = 0
        #先从左边开始，找到能够到达的最远点，并把从最远的开始到startPos的所有水果加起来，同时入队
        while p < n and fruits[p][0] <= startPos:
            if abs(fruits[p][0] - startPos) <= k:
                res += fruits[p][1]
                h.append((fruits[p][0], fruits[p][1]))
            p += 1

        tmp = res
        while p < n and fruits[p][0] - startPos <= k:
            #对于每一个startPos右端的水果，依次检查左端点是否满足条件
            while h and h[0][0] < startPos and fruits[p][0] - h[0][0] + min(startPos - h[0][0], fruits[p][0] - startPos) > k:
                tmp -= h[0][1]
                h.popleft()
            tmp += fruits[p][1]
            res = max(res, tmp)
            p += 1

        return res

# @lc code=end

