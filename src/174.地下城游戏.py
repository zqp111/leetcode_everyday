#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int: 
        M = len(dungeon)
        N = len(dungeon[0])
        Hp = [[0 for _ in range(N)] for _ in range(M)]
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                a = b = -float('inf')
                if i == M-1 and j == N-1:
                    a = b = min(dungeon[i][j], 0)
                if i != M-1:
                    a = min(dungeon[i][j] + Hp[i+1][j], 0)
                if j != N-1:
                    b = min(dungeon[i][j] + Hp[i][j+1], 0)
                if a > b:
                    Hp[i][j] = a
                else:
                    Hp[i][j] = b
        print(Hp)
        if Hp[0][0] > 0:
            return 1
        return -Hp[0][0] +1
                
# @lc code=end

