#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        tmp = []
        re = []
        self.backtracing(s, tmp, re)
        return re

    def backtracing(self, string, tmp, re):
        if len(string) == 0:
            re.append(tmp.copy())
            return
        
        for i in range(len(string)):
            if self.Is_right(string[:i+1]):
                tmp.append(string[:i+1])
                self.backtracing(string[i+1:], tmp, re)
                tmp.pop()

    def Is_right(self, strings):
        n = len(strings)
        for i in range(n//2):
            if strings[i] != strings[-i-1] :
                return False
        return True
# @lc code=end

