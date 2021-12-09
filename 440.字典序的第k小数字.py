#
# @lc app=leetcode.cn id=440 lang=python3
#
# [440] 字典序的第K小数字
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        s_list = [str(i) for i in range(1, 1+n)]
        s_list.sort()
        # print(s_list)
        a = s_list[k-1]
        return int(a)
# @lc code=end

