#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        return 0 if k % 61035156 % 12207031 % 2441406 % 488281 % 97656 % 19531 % 3906 % 781 % 156 % 31 == 30 else (not k % 61035156 % 12207031 % 2441406 % 488281 % 97656 % 19531 % 3906 % 781 % 156 % 31 % 6 // 5) * 5

# @lc code=end

