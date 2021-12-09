#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def get_n_array(n):
            if n ==1:
                return '1'
            tmp = ''
            id = ''
            re = ''
            for s in get_n_array(n-1):
                if s == tmp:
                    id += 1
                else:
                    re += str(id) + tmp
                    tmp = s
                    id = 1
            
            re += str(id) + tmp
            return re
        return get_n_array(n)
# @lc code=end

