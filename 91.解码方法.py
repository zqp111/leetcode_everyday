#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        re = [-1]*len(s)

        def get_num(strings, re):
            if len(strings) == 0:
                return 1
            if re[len(strings)-1] > -1:
                return re[len(strings)-1]
            if strings[0] == '0':
                re[len(strings)-1]=0
                return 0
            # elif int(strings[0:2]) > 26:
            #     re[len(strings)-1]=0
            #     return 0
            if len(strings) == 1:
                re[len(strings)-1]=1
                return 1
            if int(strings[0:2])<= 26:
                re[len(strings)-1] = get_num(strings[1:], re)+get_num(strings[2:], re)
            else:
                re[len(strings)-1] = get_num(strings[1:], re)
            return re[len(strings)-1]
        get_num(s, re)
        # print(re)
        return re[-1]

# @lc code=end

