#
# @lc app=leetcode.cn id=1702 lang=python3
#
# [1702] 修改后的最大二进制字符串
#

# @lc code=start
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        binary = list(binary)
        index = 0
        status = 0
        startIndex = None
        while index < len(binary):
            if status == 0:
                if binary[index] == '0':
                    status = 1
                    startIndex = index
                # index += 1
            elif status == 1:
                if binary[index] == '0':
                    binary[startIndex] = '1'
                    startIndex += 1
                    status = 1
                else:
                    status = 2
                # index += 1
            elif status == 2:
                if binary[index] == '0':
                    binary[startIndex] = '1'
                    binary[startIndex+1] = '0'
                    binary[index] = '1'
                    startIndex += 1
            index += 1
        return ''.join(binary)
                
# @lc code=end

