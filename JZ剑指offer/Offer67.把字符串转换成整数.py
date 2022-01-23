#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def strToInt(self, s: str) -> int:
        if not s: return 0

        # 消除空格
        for i in range(len(s)):
            if s[i] != ' ':
                break
        
        # 检查符号
        if s[i] == '+': 
            result = 1
            i += 1
        elif s[i] == '-': 
            result = -1
            i+=1
        else: 
            result = 1
        
        # 读取数字
        tmp = 0
        for j in range(i, len(s)):
            if not s[j].isdigit():
                break
            tmp = tmp*10 +ord(s[j])-ord('0')
            # print(tmp)
            
        result *=tmp
        if result < -(1<<31): return -(1<<31)
        if result > (1<<31)-1: return (1<<31)-1
        return result
# @lc code=end

