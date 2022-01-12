#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#

# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def get_M(a, b):
            if b == 0:
                return a
            if a< b:
                return get_M(b, a)
            return get_M(b, a%b)

        def get_mi(a, b):
            return a*b/get_M(a,b)

        tmp = ''
        A = []
        B = []
        idx = 0
        while idx < len(expression):
            if expression[idx] == '/':
                A.append(int(tmp))
                tmp = ''
            elif expression[idx] == '-':
                if tmp == '':
                    tmp += expression[idx]
                else:
                    B.append(int(tmp))
                    tmp = '-'
            elif expression[idx] == '+':
                B.append(int(tmp))
                tmp = ''
            else:
                tmp += expression[idx]
            idx += 1
        B.append(int(tmp))
        M = B[0]
        sumA = 0
        for i in range(1, len(B)):
            M = get_mi(M, B[i])
        for i in range(len(A)):
            A[i] *= M/B[i]
            sumA += A[i]
        if sumA == 0:
            return '0/1'
        q = get_M(abs(sumA), M)
        return str(int(sumA//q))+'/' + str(int(M//q))
# @lc code=end

