#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        sp = s.split('e')
        splited = []
        for i in range(len(sp)):
            splited += sp[i].split('E')
        

        if len(splited) == 1: # 两种情况 整数或者小数
            return self.isDecimalOrInteger(splited[0])
        elif len(splited) == 2: # 科学计数法
            return self.isDecimalOrInteger(splited[0]) and self.isInteger(splited[1])[1]
        else: 
            return False

    def isDecimalOrInteger(self, s):
        if not s: return False
        num = s.split('.')
        if len(num) == 1: # 整数
                return self.isInteger(num[0])[1]
        elif len(num) == 2: # 小数
            return (self.isInteger(num[0])[0] and self.isInteger(num[1])[1]) or \
                (not len(num[0]) and self.isInteger(num[1])[2]) or \
                (self.isInteger(num[0])[1] and not len(num[1]))
        else: 
            return False        

    def isInteger(self, s: str) -> bool:
        if not s: return False, False, False
        index = 0
        if s[0] == "+" or  s[0] == "-":
            index = 1
        
        if len(s) == 1 and index:
            return True, False, index != 1
        for i in range(index, len(s)):
            if not s[i].isdigit():
                return False, False, False
        
        return True, True, index != 1

# @lc code=end

