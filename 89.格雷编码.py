#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]*(1<<n)
        for i in range(len(result)):
            result[i] = i^(i>>1)
        return result
# @lc code=end

