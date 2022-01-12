#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0, 10:0, 20:0}
        for bill in bills:
            dic[bill] += 1
            if bill == 10 :
                dic[5] -= 1
                if dic[5] < 0:
                    return False
            elif bill == 20 :
                if dic[10] > 0:
                    dic[10] -= 1
                    dic[5] -= 1
                    if dic[5] < 0:
                        return False
                else:
                    dic[5] -= 3
                    if dic[5] < 0:
                        return False
        return True
# @lc code=end

