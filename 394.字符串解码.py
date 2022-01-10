#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # print(s)
        if len(s) == 0: return ''
        for i in range(0, len(s)):
            if s[i].isdigit():
                break
        else:
            return s
        left = self.decodeString(s[:i])
        
        for numIndex in range(i, len(s)):
            if not s[numIndex].isdigit():
                break
        numTimes = int(s[i:numIndex])
        # print('numTimes', numTimes)

        tmp = 0
        for j in range(numIndex, len(s)):
            if s[j] == '[':
                tmp += 1
            elif s[j] == ']':
                tmp -= 1
            if tmp == 0:
                break
        mid = self.decodeString(s[numIndex+1:j])
        right = self.decodeString(s[j+1:])
        return left + numTimes*mid + right

# @lc code=end

