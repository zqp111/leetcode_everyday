#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        tmp = []
        re = []
        self.backtracing(s, tmp, re)
        return re

    def backtracing(self, string, tmp, re):
        if len(string) == 0 and len(tmp) == 4:
            m = tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+tmp[3]
            re.append(m)
            return
        
        for i in range(max(0, len(string)-12 + len(tmp)*3),min(len(string), 3)):
            if self.Is_right(string[:i+1]):
                tmp.append(string[:i+1])
                self.backtracing(string[i+1:], tmp, re)
                tmp.pop()

    def Is_right(self, strings):
        if len(strings) != 1 and strings[0] == '0' :
            return False

        if int(strings) > 255:
            return False

        return True
# @lc code=end

