#
# @lc app=leetcode.cn id=1893 lang=python3
#
# [1893] 检查是否区域内所有整数都被覆盖
#

# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x:[x[0], -x[1]])
        l, r= ranges[0]
        tmp = []
        for li, ri in ranges[1:]:
            if ri <= r: continue
            if li<= r+1: r = max(r, ri)
            else:
                tmp.append((l, r))
                l, r = li, ri
        tmp.append((l, r))
        # print(tmp)
        for li, ri in tmp:
            if left >= li and right <= ri: return True
        return False
# @lc code=end

