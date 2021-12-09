#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        big = int(sqrt(n))
        tmp = n
        q_num = [i**2 for i in range(n+1)]
        ans_dict = {q_num[i]:1 for i in range(1, n+1)}
        
        ans_dict[0] = 0
        res = 1 + min([self.get_ans(n-q_num[i], i, ans_dict, q_num) for i in range(big, 0, -1)])
        return res

    def get_ans(self, n, big, ans_dict, q_num):
        # print(ans_dict)

        # print(n, big, ans_dict)
        if ans_dict.__contains__(n):
            return ans_dict[n]
        # if big**2 >= n :
        big = int(sqrt(n))
        res = 1 + min([self.get_ans(n-q_num[i], i, ans_dict, q_num) for i in range(big, 0, -1)])
        ans_dict[n] = res
        # print(n, res)
        return res
        # tmp = n
        # while (tmp%4==0):
        #     tmp /= 4
        #     # print(tmp)
        # if tmp % 8 == 7:
        #     return 4
        
        # if int(sqrt(n))-sqrt(n) == 0:
        #     return 1
        
        # for i in range(1, int(sqrt(n))+1):
        #     if int(sqrt(n-i**2)) - sqrt(n-i**2) ==0:
        #         return 2

        # return 3

# @lc code=end

