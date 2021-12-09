#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l = []
        l.append('qwertyuiop')
        l.append('asdfghjkl')
        l.append('zxcvbnm')
        re = []
        for str_ in words:
            if str_[0].lower() in l[0]:
                status=0
            elif str_[0].lower() in l[1]:
                status=1
            elif str_[0].lower() in l[2]:
                status=2
            flag = True
            for s in str_[1:]:
                if not (s.lower() in l[status]):
                    flag = False
            if flag:
                re.append(str_)
        return re

        
# @lc code=end

