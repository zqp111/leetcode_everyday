#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = [], []
        length = len(senate)

        for i, char in enumerate(senate):
            if char == "R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            if R[0] < D[0]:
                R.append(R.pop(0) + length)
                D.pop(0)
            else:
                D.append(D.pop(0) + length)
                R.pop(0)
        return "Radiant" if R else "Dire"
# @lc code=end

