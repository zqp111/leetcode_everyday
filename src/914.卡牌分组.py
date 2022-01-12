#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def get_max(a, b):
            if a < b:
                return get_max(b,a)
            if b == 0:
                return a
            return get_max(b,a%b)

        deck_dict = dict()
        for num in deck:
            if num in deck_dict.keys():
                deck_dict[num] += 1
            else:
                deck_dict[num] = 1
        ss = deck_dict[num]
        if ss ==1:
            return False
        for key in deck_dict.keys():
            ss=get_max(ss, deck_dict[key])
            if ss < 2:
                return False
        return True
# @lc code=end

