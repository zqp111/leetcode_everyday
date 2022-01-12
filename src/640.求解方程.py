#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        i = 0
        flag = True
        tmp = '0'
        x = 0
        c =0
        while i < len(equation):
            if equation[i] == '=':
                if tmp[-1] != 'x':
                    if flag:
                        c -= int(tmp)
                    else:
                        c += int(tmp)
                tmp = '0'
                flag = False
            elif equation[i] =="+":
                if tmp[-1] != 'x':
                    if flag:
                        c -= int(tmp)
                    else:
                        c += int(tmp)
                tmp = '0'
            elif equation[i] =="-":
                if tmp[-1] != 'x':
                    if flag:
                        c -= int(tmp)
                    else:
                        c += int(tmp)
                tmp = '-'
            elif equation[i] =="x":
                if tmp == '0' or tmp == '-':
                        tmp += '1'
                if flag:
                    x += int(tmp)
                else:
                    x -= int(tmp)
                tmp += equation[i]
            else:
                tmp += equation[i]
            i += 1
        if tmp[-1] != 'x':
            if flag:
                c -= int(tmp)
            else:
                c += int(tmp)
        if x== 0 and c==0:
            return "Infinite solutions"
        elif x ==0 :
            return "No solution"
        else:
            return "x="+str(int(c/x))
        
# @lc code=end

