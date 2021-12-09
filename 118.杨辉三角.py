#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.re = []
        if numRows == 0:
            return []
        def gen_n(n):
            if n == 1:
                self.re.append([1])
                return [1]
            re = list()
            # print(gen_n(n-1))
            m = gen_n(n-1)
            m.insert(0,0)
            m.append(0)
            for i in range(len(m)-1):
                re.append(m[i]+m[i+1])
            # print(re)
            self.re.append(re.copy())
            return re
        gen_n(numRows)
        return self.re

# @lc code=end

