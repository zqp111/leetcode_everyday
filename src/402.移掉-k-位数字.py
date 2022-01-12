#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # 消除简单特例
        if len(num) <= k:
            return '0'
        # 每次考虑k+1个元素，删除其中一个使其当前最小，直至完成
        ## 删除的元素为倒序排列的开始

        # end = k
        # now_arr
        # for i in range(k): # 删除k个

        #     if end!=len(num): # 非最后一个，添加一位
        #         k = k+1
        def pop(string, index=0):
            if index == 0:
                return string[1:]
            elif index == len(string)-1 or index==-1:
                return string[:index]
            return string[:index] + string[index+1:]
            

        s = 0
        pop_num = 0
        while pop_num < k:
            # print(s, num)
            if s == len(num)-1: # 到最后一个
                pop_num += 1
                num = pop(num, -1)
                s -= 1
                continue
            if int(num[s]) <= int(num[s+1]):
                s += 1
            else:
                pop_num += 1
                num = pop(num, s)
                if s != 0:
                    s -= 1

        for i in range(len(num)-1):
            if num[i] == '0':
                pass
            else:
                return num[i:]
        return num[-1]
        


# @lc code=end

