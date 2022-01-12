#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:

        tmpNum = num
        i = 0
        numDict = 'IVXLCDM'
        result = ''
        while tmpNum:
            tmpNum, curNum = divmod(tmpNum, 10)
            if curNum == 9:
                result = numDict[i] + numDict[i+2] + result
            else:
                if curNum >= 5:
                    result = numDict[i+1] + numDict[i]*(curNum-5) + result
                elif curNum == 4:
                    result = numDict[i] + numDict[i+1] + result
                else:
                    result = numDict[i]*curNum + result
            i += 2
        return result

# @lc code=end

