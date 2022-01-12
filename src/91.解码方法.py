#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        # re = [-1]*len(s)

        # def get_num(strings, re):
        #     if len(strings) == 0:
        #         return 1
        #     if re[len(strings)-1] > -1:
        #         return re[len(strings)-1]
        #     if strings[0] == '0':
        #         re[len(strings)-1]=0
        #         return 0
        #     # elif int(strings[0:2]) > 26:
        #     #     re[len(strings)-1]=0
        #     #     return 0
        #     if len(strings) == 1:
        #         re[len(strings)-1]=1
        #         return 1
        #     if int(strings[0:2])<= 26:
        #         re[len(strings)-1] = get_num(strings[1:], re)+get_num(strings[2:], re)
        #     else:
        #         re[len(strings)-1] = get_num(strings[1:], re)
        #     return re[len(strings)-1]
        # get_num(s, re)
        # # print(re)
        # return re[-1]
        dp = [0]*(len(s)+1)
        dp[-1] = dp[-2] = 1
        if s[-1] == '0': dp[-2] = 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0': 
                dp[i] = 0
            elif int(s[i:i+2]) <=26:
                dp[i] = dp[i+1]+dp[i+2]
            else:
                dp[i] = dp[i+1]
        return dp[0]
            
# @lc code=end

