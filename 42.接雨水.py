#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        a = []
        b = []
        max_ = 0
        ans = 0
        for i in range(len(height)):
            if height[i] >max_:
                max_ = height[i]
            a.append(max_ - height[i])
        max_ = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] >max_:
                max_ = height[i]
            b.insert(0, max_ - height[i])
        for i in range(len(height)):
            ans += min(a[i], b[i])
        # print(a, b)
        return ans
# @lc code=end

