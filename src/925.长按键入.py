#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        for i in range(len(typed)):
            if not name:
                if  i>0 and typed[i] != typed[i-1]:
                    return False
                continue
            if typed[i] == name[0]:
                name = name[1:]
            elif i>0 and typed[i] == typed[i-1]:
                continue
            else:
                return False
        return not name
# @lc code=end

