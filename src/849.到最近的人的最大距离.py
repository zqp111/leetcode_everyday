#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        status = 0
        tmp = 0
        ans = 1
        # for seat in seats:
        #     if status == 0:
        #         if seat == 0:
        #             tmp += 1
        #         else:
        #             ans = max(ans, tmp)
        #             status = 1
        #             tmp = 0
        #     elif status == 1:
        #         if seat == 0:
        #             tmp += 1
        #         else:
        #             nowDis = tmp//2 + (tmp%2)
        #             ans = max(ans, nowDis)
        #             tmp = 0

        for seat in seats:
            if seat == 0:
                    tmp += 1
            elif status == 0:
                ans = max(ans, tmp)
                status = 1
                tmp = 0
            elif status == 1:
                nowDis = tmp//2 + (tmp%2)
                ans = max(ans, nowDis)
                tmp = 0

        if status == 1 and seats[-1] == 0:
            ans = max(ans, tmp)
        return ans
# @lc code=end

